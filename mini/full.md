
# Full版ファームウェア

Full版ファームウェアでは、[Keyboard Quantizer Config Generator](https://sekigon-gonnoc.github.io/keyboard-quantizer-config-generator/)を使用して設定ファイルを作成し、デバイスに書き込むことでキーマップを変更します。

テキスト形式の設定ファイルを使ってRemapより多くの項目（コンボ、オーバーライド、タップダンス、リーダー）を設定できます。

Windowsの場合はコンパニオンアプリを実行することで、アクティブなアプリに応じてキーマップを切り替えたり、キーボードからユニコード文字を送信することもできます。コンパニオンアプリはPowerShellスクリプトで実装されており、キーボードからPCに送信して実行できるため、PCに追加のソフトウェアをインストールする必要はありません。（Windows 10で動作確認）

## 設定の更新方法

- [Keyboard Quantizer Config Generator](https://sekigon-gonnoc.github.io/keyboard-quantizer-config-generator/)にアクセスし、設定ファイルを記入します。設定ファイルの書き方やサンプルについては[別ページ](full_config.md)にまとまっています
- `Download UF2`ボタンをクリックしuf2形式で設定ファイルをダウンロードします
- デバイスのブートローダを起動し、作成したuf2ファイルをコピーすることで設定が更新されます
- `Upload`ボタンから設定ファイルを読み込むことで、作成した設定を読み込んで再編集することもできます
- 設定が正しく動作するには、設定ファイルのバージョンとファームウェアのバージョンが一致している必要があります。ファームウェア更新前には設定ファイルのバックアップを取って、設定サイトで読み込みなおして最新バージョン向けに変換しなおしてください。


OSがWindowsの場合のみ、コンパニオンアプリを使用して下記の方法で書き込み・読み込みができます。

- 設定ファイルをbin形式でダウンロードし、コンパニオンアプリのタスクトレイアイコンを右クリックして、`Load config to device`から書き込みたいファイルを選択することで設定が更新されます
- デバイスに書き込まれている設定ファイルを読み込む場合、コンパニオンアプリのタスクトレイアイコンを右クリックし、`Backup config from device`を実行してください

## ファームウェアのビルド

ファームウェア自体に変更を加えたい場合はファームウェアをビルドしてください。

[https://github.com/sekigon-gonnoc/qmk_firmware/tree/keyboard/sekigon/keyboard_quantizer/mini-full](https://github.com/sekigon-gonnoc/qmk_firmware/tree/keyboard/sekigon/keyboard_quantizer/mini-full)

```
qmk compile -kb sekigon/keyboard_quantizer/mini -km full
```

## コンパニオンアプリの常駐設定

[コンパニオンアプリ](https://github.com/sekigon-gonnoc/qmk_firmware/blob/keyboard/sekigon/keyboard_quantizer/mini-full/keyboards/sekigon/keyboard_quantizer/mini/keymaps/full/dynamic_config/quantizer_companion.ps1)のPowerShellスクリプトをスタートアップに登録してください。引数として接続先のKeyboard QuantizerのCOMポートが必要です。