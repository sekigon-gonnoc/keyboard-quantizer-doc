# Keyboard Quantizer ビルドガイド(Rev3)

![rev3](img/rev3_rear.jpg)

- [販売リンク](#販売リンク)
- [キット内容](#キット内容)
- [組み立て](#組み立て)
- [ファームウェア(QMK)](#ファームウェアqmk)
- [(未組立版の組立時など)ホスト用ファームの書きこみ](#未組立版の組立時などホスト用ファームの書きこみ)
- [キーマップ一覧](#キーマップ一覧)
- [キーマップのオプション](#キーマップのオプション)
  - [レポートパーサの設定](#レポートパーサの設定)
  - [仮想シリアルポート](#仮想シリアルポート)
  - [LEDの制御](#ledの制御)
  - [ファームウェアを小さくする](#ファームウェアを小さくする)
  - [VIA対応](#via対応)

## 販売リンク
- [BOOTH](https://nogikes.booth.pm/items/2256612)
- [遊舎工房](https://yushakobo.jp/shop/keyboard-quantizer/)

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
  ![rev3_build](img/rev3_build.jpg)
- ケースを開けるときはマイナスドライバーなど薄いものを側面の隙間にいれてこじ開けてください
  - 鋭利な工具を使用する場合は怪我に注意してください

## ファームウェア(QMK)
- rev3はatmega32u4を内蔵しています。書き込むファームウェアは[このリポジトリ](https://github.com/sekigon-gonnoc/qmk_firmware/tree/dev/sekigon)のdev/sekigonブランチです
- 未組立版の場合、最初に組み立てるときはbootloaderキーマップを書き込んでください。次の手順に必要です。
  - [キーマップ一覧](#キーマップ一覧)
    ```bash
        # qmk_quantizerというフォルダ名でリポジトリをクローン
        git clone https://github.com/sekigon-gonnoc/qmk_firmware.git -b dev/sekigon qmk_quantizer
        # bootloaderキーマップを書きこみ
        make keyboard_quantizer/rev3:bootloader:flash
    ```
- キーマップのオプションについては後述の説明を確認してください
- ブートローダを以下のいずれかの手順で起動できます
  - Quantizerにキーボードを挿していない状態でPCに接続する
  - キーマップに割り当てたRESETキーを押す
  - (defaultキーマップ)シリアルポートを1200bpsで開いてから閉じる

## (未組立版の組立時など)ホスト用ファームの書きこみ
- atmega32u4を経由してUSBホスト用のICにファームを書き込みます
- Python 3.7以上が必要です
- atmega32u4にbootloaderキーマップのファームが書き込まれている前提です

  ```bash
  # COMポート名をデバイスマネージャ等で確認して指定
  ./ch559update.py flash -p <COM port> -f CH559USB.bin
  ```

  - 実行時にエラーが出る場合はpyserialを追加してください
     ```
      pip install pyserial
     ```

  - 以下のメッセージが表示されたら完了です。PCから抜き差しして電源を入れ直してください
    ```
      Chip erase start...
      Chip erase complete.
      Flash start...
      .............................................................................................................................................................................................................................................................................................................
      Flash complete.
      Verify start...
      .............................................................................................................................................................................................................................................................................................................
      Verify complete.
    ```

## キーマップ一覧
- default
  - デフォルトパーサを使ったファームウェア
- bootloader
  - ホストICのアップデートのためのファームウェア
- via
  - VIA/Remapからキーマップを書き換えるためのファームウェア
- fixed
  - fixedパーサを使ったファームウェア
- mouse
  - マウス/トラックボールの動作を変更するためのファームウェア

## キーマップのオプション
### レポートパーサの設定
- キーボード(HIDデバイス)が送信するレポートを解釈する関数を3つのオプションから設定できます
   |オプション|特徴|
   |-|-|
   |default|レポートディスクリプタを使ってレポートを解釈する。<br>ファームの容量が大きくなる代わりにNKROやポインティングデバイス付きのキーボードが動作する可能性がある|
   |fixed|6KROのキーボードのみ動作する、以前のファームと同じ動作。ファームの容量が小さい|
   |user|keymap.cなどに独自のパーサを実装する|
- デフォルトパーサから変更するにはビルド時にオプションとして`PARSER=<parser>`を追加するか、config.hで指定してください
  ```bash
    make keyboard_quantizer/rev3:default PARSER=fixed
    # or 
    make keyboard_quantizer/rev3:default PARSER=default
  ```

  ```c
  #undef QUANTIZER_REPORT_PARSER

  // Use fixed parser. Enabled for 'fixed' keymap
  #define QUANTIZER_REPORT_PARSER REPORT_PARSER_FIXED
  //or use default parser 
  #define QUANTIZER_REPORT_PARSER REPORT_PARSER_DEFAULT
  ```

### 仮想シリアルポート
- virtserを有効にするとシリアルポートからデバッグ情報を読み出したりブートローダを起動したりできます
  |コマンド|機能|
  |-|-|
  |d|デバッグ出力有効化/無効化|
  |b|ブートローダ起動|

- 機能を無効化するとファームウェアのサイズを小さくできます
  ```makefile
  VIRTSER_ENABLE = no
  ```

### LEDの制御
- `void update_indicator_led(void)`を定義することでインジケータLEDを制御できます
  - デフォルトの状態だと本来の機能(NumLock, CapsLock)を点滅で表示し、レイヤ状態を点灯で表示します

### ファームウェアを小さくする
  - parserをfixedにする
  - virtserを無効にする
  - viaを無効にする
  - consoleを無効にする

その他QMKのドキュメントを参考にしてください


### VIA対応
- viaキーマップはVIA Configuratorに対応しています
  - レイヤ数の初期値は6で、設定変更でより増やすこともできます
  - VIA Configuratorからキーマップを書き換えるには[keyboard-quantizer.json](keyboard-quantizer.json)を読み込ませてください
- 独自のキーマップをVIAに対応させる場合はrules.mkに以下のオプションを指定してください
  ```makefile
  VIA_ENABLE = yes
  VIRTSER_ENABLE = no # to avoid EP count limit                             
  ```
