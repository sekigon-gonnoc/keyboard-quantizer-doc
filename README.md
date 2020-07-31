# Keyboard Quantizer ビルドガイド
Keyboard Quantizerは一般的なUSBキーボードを自作キーボード用のファームウェアの定番であるQMKに対応させるためのボードです。キー配列を自由に変えられるだけでなく、キーボードにレイヤ、マクロ、コンビネーションなどの機能を追加できるようになります。

2個のUSBポートがあるので最大で2台のキーボードを接続できます。また、ファームウェアを開発することによってマウスなどその他のHID機器も接続できます。

## 制約事項
簡単な仕組みとしては、1. USBホスト用のマイコンがUSB機器と通信し、2. 受け取ったレポートをボード上のPro Microに送信、3. Pro Microはレポートから押されたキーを判定してQMK上の処理をする、といった流れになっています。

そのため、Fnキーなどのレポートとしては送信されないキーに反応することはできません。Fnキーと他のキーの組み合わせにより入力されるキー/音量調整などのレポートは受け取ることができます。

現時点で実装が完了しているファームウェアはキーボードから送信されるレポートがブートプロトコル(いわゆる6KROのこと。モディファイア+予約(1byte)+6キー分のデータを送信する)であることを前提としています。

この前提を満たさないキーボード(NKRO対応しているものなど)で使う場合にはファームウェアを改造する必要があります。

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
|Pro Micro (BLE Micro Proには対応していません)|1|
|コンスルーまたはピンヘッダ/ソケット|適量|

- お好みに応じてOLEDを取り付けることもできます
- USBホスト用ICのファームを書き換える場合にはUSB-UARTブリッジが必要です

## 組み立て
- USBコネクタ、タクトスイッチ、Pro Microをはんだ付けしたら完成です
- ケースが欲しい場合は添付の図面を参考にしてください

## ボタンの説明
- RST(Pro Microに近いスイッチ)
    - Pro Microをリセットする。QMKファームウェアを書き込むときに使う
- BOOT(Pro Microから遠いスイッチ)
    - このボタンを押しながら電源を入れると、USBホストICのブートローダが起動する。USBホストICのファームウェアをアップデートするときに使う

## ファームウェア
- Pro Microに書き込むファームウェアは[このリポジトリ](https://github.com/sekigon-gonnoc/qmk_firmware/tree/dev/quantizer)のdev/quantizerブランチです
    ```
        git pull https://github.com/sekigon-gonnoc/qmk_firmware.git -b dev/quantizer qmk_quantizer
        make keyboard_quantizer:default:flash
    ```
- VIAキーマップはVIA Configuratorに対応していますがeepromのサイズの都合上で2レイヤまでしか変更できないため、より多くのレイヤを使いたい場合はdefaultキーマップを改造してください