# Keyboard Quantizer ビルドガイド(Rev3)

![rev3](img/rev3_rear.jpg)

## キット内容
本キットには以下の部品が入っています

|部品|数量|
|--|--|
|メイン基板(表面実装部品実装済み) |1
|USBプラグ |1
|USBレセプタクル |1
|ケース |1

## 組み立て
- USBコネクタをはんだ付けし、ケースに入れます
- ケースを開けるときはマイナスドライバーなど薄いものを側面の隙間にいれてこじ開けてください
  - 鋭利な工具を使用する場合は怪我に注意してください

## ファームウェア
- rev3はatmega32u4を内蔵しています。書き込むファームウェアは[このリポジトリ](https://github.com/sekigon-gonnoc/qmk_firmware/tree/dev/sekigon)のdev/sekigonブランチです
    ```
        git clone https://github.com/sekigon-gonnoc/qmk_firmware.git -b dev/sekigon qmk_quantizer
        make keyboard_quantizer/rev3:via:flash
    ```
- VIAキーマップはVIA Configuratorに対応しています
  - レイヤ数の初期値は6で、設定変更でより増やすこともできます
  - VIA Configuratorからキーマップを書き換えるには[keyboard-quantizer.json](keyboard-quantizer.json)を読み込ませてください
- ブートローダを起動するにはキーマップにRESETを割り当ててください
  - defaultキーマップではシリアルポートを1200bpsで開いてから閉じることでも起動できます