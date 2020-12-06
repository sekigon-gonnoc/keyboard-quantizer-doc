# Keyboard Quantizer ビルドガイド(~Rev2)

## キット内容
本キットには以下の部品が入っています

|部品|数量|
|--|--|
|メイン基板(表面実装部品実装済み) |1
|USBコネクタ |2
|タクトスイッチ |2
|ねじ、スペーサ |4

## キット以外に必要な部品

本キットを完成させるには以下の部品が追加で必要です

|部品|数量|
|--|--|
|Pro Micro または BLE Micro Pro|1|
|コンスルーまたはピンヘッダ/ソケット|適量|

- お好みに応じてOLEDを取り付けることもできます
- USBホスト用ICのファームを書き換える場合にはUSB-UARTブリッジが必要です

## 組み立て
- USBコネクタ、タクトスイッチ、Pro Microをはんだ付けしたら完成です
- ケースが欲しい場合は添付の図面を参考にしてください
- バージョンによってLCDの取り付け向きが異なるのでシルクをよく確認してください

## ボタンの説明
- RST(Pro Microに近いスイッチ)
    - Pro Microをリセットする。QMKファームウェアを書き込むときに使う
- BOOT(Pro Microから遠いスイッチ)
    - このボタンを押しながら電源を入れると、USBホストICのブートローダが起動する。USBホストICのファームウェアをアップデートするときに使う

## ファームウェア
### Pro Microの場合
- Pro Microに書き込むファームウェアは[このリポジトリ](https://github.com/sekigon-gonnoc/qmk_firmware/tree/dev/quantizer)のdev/quantizerブランチです
    ```
        git clone https://github.com/sekigon-gonnoc/qmk_firmware.git -b dev/quantizer qmk_quantizer
    ```
    - アルファ版
    ```
        make keyboard_quantizer/rev1:default:flash
    ```
    - ベータ版
    ```
        make keyboard_quantizer/rev2:default:flash
    ```
- VIAキーマップはVIA Configuratorに対応しています
  - VIA Configuratorからキーマップを書き換えるには[keyboard-quantizer.json](keyboard-quantizer.json)を読み込ませてください
  - アルファ版の場合は内蔵eepromのサイズの都合上で2レイヤまでしか変更できないため、より多くのレイヤを使いたい場合はdefaultキーマップを改造してください
  - ベータ版は外付けeepromを使うことでVIA用のレイヤを増やすことができます。初期値は6で、設定変更でより増やすこともできます

### BLE Micro Proの場合
- BLE Micro Pro Web Configuratorを使ってください
  - レイヤの最大数は4です