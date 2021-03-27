# 自分でレポートパーサを実装する

## サンプル

- Thinkpad trackpoint keyboard専用のパーサを実装した[サンプル](https://github.com/sekigon-gonnoc/qmk_firmware/blob/dev/sekigon/keyboards/keyboard_quantizer/keymaps/user_parser_sample/keymap.c)

## 編集するファイルと関数
- 自分で用意したパーサを使用するにはconfig.hへのオプション追加とkeymap.cへの関数の実装が必要です
### config.h
- 下記のオプションを追加
  ```c
   // Use user parser
  #undef QUANTIZER_REPORT_PARSER
  #define QUANTIZER_REPORT_PARSER REPORT_PARSER_USER 
  ```

### keymap.c
- `void report_descriptor_parser_user(uint8_t interface, uint8_t const* desc, uint16_t len)`
  - 受信したレポートディスクリプタを解析する
  - サンプルでは特定のキーボードの種類を想定しているのでレポートディスクリプタは解析不要のため、空の関数

- `void on_disconnect_device_user(uint8_t device)`
  - Quantizerからデバイスを抜いたときに実行する関数
  - サンプルではキーが押しっぱなしにならないように受信したデータをクリアしている

- `bool report_parser_user(uint8_t const* buf, uint16_t len, matrix_row_t* current_matrix)`
  - 受信したレポートを解析しキーマトリクスを更新する。戻り値はマトリクスの更新の有無
  - サンプルではVID:PIDがトラックポイントキーボードと一致した場合は専用の関数を、それ以外では6KROキーボード用の関数を呼び出している

## レポートの形式を調べる
[defaultキーマップ](https://github.com/sekigon-gonnoc/keyboard-quantizer-doc/releases/download/0.3.1/keyboard_quantizer_rev3_default.hex)のデバッグ機能を使ってどんなレポートが送られてくるか調べられます

- defaultキーマップの書き込み
  - `make keyboard_quantizer/rev3:default:flash`
- TeraTermなどでシリアルポートを開く(ボーレートは1200bps以外)
- シリアルポートから`d`を送信
  - デバッグプリントが表示される
  ```
  d
  Enable dprint
  matrix scan frequency: 3762
  ```
- キーを押したりマウスを操作したときのレポートを確認
  - 先頭10バイトはホストICが付加したヘッダ
  - サンプルの場合以下の三種類 
  ```bash
  # Aキーを押したとき
  Receive: device:0, ep:1
  08 00 04 06 00 01 EF 17 47 60 00 00 04 00 00 00 00 00
  #<------    header     ----->|<-------report-------->

  # カーソルを動かしたとき
  Receive: device:1, ep:2
  06 00 04 02 01 02 EF 17 47 60 01 00 00 02 00 00
  #<------    header     ----->|<----report----->

  # 横スクロールしたとき
  Receive: device:1, ep:2
  03 00 04 02 01 02 EF 17 47 60 16 FF 00
  #<------    header     ----->|<report>
  ```
    - device0はキーボード
    - device1のID0はマウス(横スクロールは除く、xyは8bit)、ID0x16は横スクロール
