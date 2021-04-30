#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import argparse
import serial
import logging

PACKET_HEADER = [0x57, 0xab]
DETECT_CMD = [
    0xa1, 0x12, 0x00, 0x59, 0x11, 0x4d, 0x43, 0x55, 0x20, 0x49, 0x53, 0x50,
    0x20, 0x26, 0x20, 0x57, 0x43, 0x48, 0x2e, 0x43, 0x4e
]
RESET_CMD = [0xa2, 0x01, 0x00, 0x01]
KEY_CMD = [0xa3, 0x22, 0x00] + [0x00] * 0x22
ERASE_CMD = [0xa4, 0x01, 0x00, 0x00]
WRITE_CMD = [0xa5, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
VERIFY_CMD = [0xa6, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
READ_CFG_CMD = [0xa7, 0x02, 0x00, 0x1f, 0x00]

PAGE_MAX = 60


def __dumpHex(arg):
    return ' '.join([format(h, '02x') for h in arg])


def __convertPayload(payload, chksum, devid):
    for idx in range(len(payload)):
        if idx % 8 == 0x07:
            payload[idx] = (payload[idx] ^ ((chksum + devid) & 0xFF)) & 0xFF
        else:
            payload[idx] = (payload[idx] ^ chksum) & 0xFF


def __appendHeader(packet):
    return PACKET_HEADER + packet


def __appendChecksum(packet):
    s = (0x55 + 0xab + sum(packet)) & 255
    return packet + [s]


def __makeFlashCmd(cmdheader, address, remain, payload, chksum, devid):

    cmd = cmdheader
    cmd[1] = len(payload) + 5
    cmd[3] = address & 0xff
    cmd[4] = (address >> 8) & 0xff
    cmd[7] = remain & 0xff

    __convertPayload(payload, chksum, devid)

    cmd = cmd + payload
    cmd = __appendChecksum(cmd)
    return __appendHeader(cmd)


def __makeFlashWriteCmd(address, remain, payload, chksum, devid):
    return __makeFlashCmd(WRITE_CMD, address, remain, payload, chksum, devid)


def __makeVerifyCmd(address, remain, payload, chksum, devid):
    return __makeFlashCmd(VERIFY_CMD, address, remain, payload, chksum, devid)


def __makeEraseCmd(byte_len):
    cmd = ERASE_CMD
    page_len = math.floor((byte_len + 1024 - 1) / 1024)

    if page_len > PAGE_MAX:
        raise Exception(f'File size is too large({byte_len}>{1024*PAGE_MAX}).')

    cmd[3] = page_len
    cmd = __appendChecksum(cmd)
    return __appendHeader(cmd)


def __makeDetectCmd():
    cmd = DETECT_CMD
    cmd = __appendChecksum(cmd)
    return __appendHeader(cmd)


def __makeResetCmd():
    cmd = RESET_CMD
    cmd = __appendChecksum(cmd)
    return __appendHeader(cmd)


def __makeReadCfgCmd():
    cmd = READ_CFG_CMD
    cmd = __appendChecksum(cmd)
    return __appendHeader(cmd)


def __makeSendKeyCmd():
    cmd = KEY_CMD
    cmd = __appendChecksum(cmd)
    return __appendHeader(cmd)


def __splitToChunk(binfile, size):
    for idx in range(0, len(binfile), size):
        yield binfile[idx:idx + size]


def __flashBinFile(binfile, com, checksum, devid):
    chunks = __splitToChunk(binfile, 56)

    addr = 0
    remains = len(binfile)

    for chunk in chunks:
        if len(chunk) < 56:
            chunk.extend([0xFF] * (56 - len(chunk)))
        cmd = __makeFlashWriteCmd(addr, remains, chunk, checksum, devid)
        addr = addr + len(chunk)
        remains = remains - len(chunk)
        com.write(cmd)
        logging.debug('send:' + __dumpHex(cmd))
        ret = com.read(size=9)
        if len(ret) != 9 or ret[6] != 0:
            raise Exception(f'Flash failed at address {addr}')
        logging.debug('receive:' + __dumpHex(ret))
        print('.', end='', flush=True)


def __verifyBinFile(binfile, com, checksum, devid):
    chunks = __splitToChunk(binfile, 56)

    addr = 0
    remains = len(binfile)

    for chunk in chunks:
        if len(chunk) < 56:
            chunk.extend([0xFF] * (56 - len(chunk)))
        cmd = __makeVerifyCmd(addr, remains, chunk, checksum, devid)
        addr = addr + len(chunk)
        remains = remains - len(chunk)
        com.write(cmd)
        logging.debug('send:' + __dumpHex(cmd))
        ret = com.read(size=9)
        if ret[6] != 0:
            raise Exception(
                f'verify failed at address {addr - len(chunk)} to {addr}')
        logging.debug('receive:' + __dumpHex(ret))
        print('.', end='', flush=True)


def __detectCh559(com):
    if not com.isOpen():
        raise
    cmd = __makeDetectCmd()
    ret = com.write(cmd)
    logging.debug('send:' + __dumpHex(cmd))
    ret = com.read(size=9)
    if len(ret) < 9 or ret[5] != 0:
        raise Exception('CH559 is not found.')
    logging.debug('receive:' + __dumpHex(ret))


def __getCfg(com):
    if not com.isOpen():
        raise
    cmd = __makeReadCfgCmd()
    ret = com.write(cmd)
    logging.debug('send:' + __dumpHex(cmd))
    ret = com.read(size=33)
    if (ret[5] != 0):
        return None
    logging.debug('receive:' + __dumpHex(ret))

    version = f'ver{ret[21]}.{ret[22]}{ret[23]}'
    checksum = sum(ret[24:28]) & 0xff

    return {'version': version, 'checksum': checksum}


def __sendKey(com):
    if not com.isOpen():
        raise
    cmd = __makeSendKeyCmd()
    logging.debug('send:' + __dumpHex(cmd))
    ret = com.write(cmd)
    ret = com.read(size=9)
    if (ret[5] != 0):
        raise
    logging.debug('receive:' + __dumpHex(ret))


def __eraseChip(com, filesize):
    cmd = __makeEraseCmd(filesize)
    ret = com.write(cmd)
    logging.debug('send:' + __dumpHex(cmd))
    ret = com.read(size=9)
    if (ret[5] != 0):
        raise
    logging.debug('receive:' + __dumpHex(ret))


def __restartUserCode(com):
    cmd = __makeResetCmd()
    ret = com.write(cmd)
    logging.debug('send:' + __dumpHex(cmd))
    ret = com.read(size=9)
    logging.debug('receive:' + __dumpHex(ret))


def __ch559flash(args, com):
    if com is None:
        print('No COM port')
        return

    __detectCh559(com)
    cfg = __getCfg(com)

    if args.file != '':

        with open(args.file, 'rb') as f:
            binfile = list(f.read())

            print('Chip erase start...')
            __eraseChip(com, len(binfile))
            print('Chip erase complete.')

            __sendKey(com)

            print('Flash start...')
            __flashBinFile(binfile, com, cfg['checksum'], 0x59)
            print('')
            print('Flash complete.')

            __sendKey(com)

            # print(f'checksum:{cfg['checksum']}')

            print('Verify start...')
            __verifyBinFile(binfile, com, cfg['checksum'], 0x59)
            print('')
            print('Verify complete.')


def __ch559verify(args, com):
    if com is None:
        print('No COM port')
        return

    __detectCh559(com)
    cfg = __getCfg(com)

    if args.file != '':

        __sendKey(com)

        with open(args.file, 'rb') as f:
            binfile = list(f.read())
            print('Verify start...')
            __verifyBinFile(binfile, com, cfg['checksum'], 0x59)
            print('')
            print('Verify complete.')


def __ch559update():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, default='')
    parser.add_argument('-p', '--port', type=str, default='')
    parser.add_argument('-r', '--reset', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')

    subparsers = parser.add_subparsers()

    parser_flash = subparsers.add_parser('flash',
                                         parents=[parser],
                                         add_help=False)
    parser_flash.set_defaults(handler=__ch559flash)

    parser_verify = subparsers.add_parser('verify',
                                          parents=[parser],
                                          add_help=False)
    parser_verify.set_defaults(handler=__ch559verify)

    args = parser.parse_args()

    com = None
    if args.port != '':
        com = serial.Serial(port=args.port, baudrate=57600, timeout=5)

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)-15s %(message)s')
    else:
        logging.basicConfig(level=logging.INFO)

    if hasattr(args, 'handler'):
        args.handler(args, com)

    if args.reset and args.port != '':
        print('Reset target...')
        __restartUserCode(com)
        print('Reset complete.')


if __name__ == '__main__':
    __ch559update()
