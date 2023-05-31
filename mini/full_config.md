
- [設定ファイルの書き方](#設定ファイルの書き方)
  - [yamlファイルの各キーの説明](#yamlファイルの各キーの説明)
    - [`application`](#application)
    - [`application.title`, `application.process`, `application.url`](#applicationtitle-applicationprocess-applicationurl)
    - [`application.os`](#applicationos)
    - [`application.keymaps`](#applicationkeymaps)
    - [`application.keymaps.keymap`](#applicationkeymapskeymap)
    - [`application.keymaps.keymap.layer`](#applicationkeymapskeymaplayer)
    - [`application.keymaps.keymap.map`](#applicationkeymapskeymapmap)
    - [`application.combos`](#applicationcombos)
    - [`application.combos.combo`](#applicationcomboscombo)
    - [`application.combos.combo.keys`](#applicationcomboscombokeys)
    - [`application.combos.combo.keycode`](#applicationcomboscombokeycode)
    - [`application.combos.combo.term`](#applicationcomboscomboterm)
    - [`application.combos.combo.only`](#applicationcomboscomboonly)
    - [`application.combos.combo.press_in_order`](#applicationcomboscombopress_in_order)
    - [`application.combos.combo.layer`](#applicationcomboscombolayer)
    - [`application.leaders`](#applicationleaders)
    - [`application.leaders.leader`](#applicationleadersleader)
    - [`application.leaders.leader.keys`](#applicationleadersleaderkeys)
    - [`application.leaders.leader.keycode`](#applicationleadersleaderkeycode)
    - [`application.overrides`](#applicationoverrides)
    - [`application.overrides.(basic|w_layer|w_layer_neg|w_layer_neg_opt)`](#applicationoverridesbasicw_layerw_layer_negw_layer_neg_opt)
    - [`per_key_option`](#per_key_option)
    - [`per_key_option.<keycode>.tapping_term`](#per_key_optionkeycodetapping_term)
    - [`per_key_option.<keycode>.quick_tap_term`](#per_key_optionkeycodequick_tap_term)
    - [`per_key_option.<keycode>.permissive_hold`](#per_key_optionkeycodepermissive_hold)
    - [`per_key_option.<keycode>.hold_on_other_key_press`](#per_key_optionkeycodehold_on_other_key_press)
    - [`per_key_option.<keycode>.retro_tapping`](#per_key_optionkeycoderetro_tapping)
    - [`default`](#default)
    - [`default.combo_term`](#defaultcombo_term)
    - [`default.combo_press_in_order`](#defaultcombo_press_in_order)
    - [`default.tapping_term`](#defaulttapping_term)
    - [`default.quick_tap_term`](#defaultquick_tap_term)
    - [`default.permissive_hold`](#defaultpermissive_hold)
    - [`default.hold_on_other_key_press`](#defaulthold_on_other_key_press)
    - [`default.retro_tapping`](#defaultretro_tapping)
    - [`default.keyboard_language`](#defaultkeyboard_language)
    - [`default.os_language`](#defaultos_language)
    - [`default.mouse_gesture`](#defaultmouse_gesture)
  - [設定可能な動作一覧](#設定可能な動作一覧)
    - [キーコード](#キーコード)
    - [マクロ](#マクロ)
    - [タップダンス](#タップダンス)
    - [コマンド](#コマンド)
    - [ユニコード文字列](#ユニコード文字列)
- [設定例](#設定例)


## 設定ファイルの書き方

設定ファイルはyaml形式です

### yamlファイルの各キーの説明

#### `application`

キーマップやコンボ等をグループ化します

#### `application.title`, `application.process`, `application.url`

(省略可能) コンパニオンアプリを併用する場合に、設定値と現在アクティブなウィンドウのタイトル、プロセス名、URL（ウィンドウがedge, chrome, firefoxの場合のみ）が一致するときのみ、各キーマップやコンボ等が有効になります。各設定には正規表現を使用できます。`title`, `process`, `url`, `os` を合わせて設定した場合は、AND条件として評価されます。

#### `application.os`

(省略可能) 設定値と接続先のOSが一致するときのみ、各キーマップやコンボ等が有効になります。`title`, `process`, `url` と合わせて設定した場合は、AND条件として評価されます。

#### `application.keymaps`

レイヤごとのキーマップをグループ化します。

キーマップの詳細についてはQMKのドキュメントを参照してください。

#### `application.keymaps.keymap`

キーマップのレイヤを定義します。

#### `application.keymaps.keymap.layer`

キーマップのレイヤ番号を設定します。設定可能範囲は0-15です。

#### `application.keymaps.keymap.map`

`<from>: <to>`の形式で置き換え前のキーと置き換え後の動作を設定します。

`<from>`にはQMKで定義されているキーボード、マウスのキーコードを設定します。

`<to>`に設定可能な動作については[設定可能な動作一覧](#設定可能な動作一覧)に記載しています。

置き換えを設定しないキーについてはレイヤによって下記のように扱われます。
- レイヤ0: 置き換えなし
- レイヤ1以降:`KC_TRNS`

#### `application.combos`

コンボをグループ化します

#### `application.combos.combo`

コンボを定義します。

コンボの詳細についてはQMKのドキュメントを参照してください。

#### `application.combos.combo.keys`

コンボを実行するキーの組み合わせを設定します。

`application.keymaps.keymap.map`で設定した置き換え後のキーで指定してください。

#### `application.combos.combo.keycode`

コンボを入力したときに実行するキーコードを設定します。

動作一覧のうちタップダンス以外の動作を設定できます

#### `application.combos.combo.term`

`COMBO_TERM`を設定します。

省略した場合は`default.combo_term`の値が使用されます。

#### `application.combos.combo.only`

`tap`または`hold`を指定します。それぞれQMKの`COMBO_MUST_TAP`, `COMBO_MUST_HOLD`に相当します。

省略した場合はいずれも設定されません。

#### `application.combos.combo.press_in_order`

`true`に設定した場合`combo.keys`の順番に押下したときのみコンボが成立します。

省略した場合は`default.combo_press_in_order`の値が使用されます

#### `application.combos.combo.layer`

現在のレイヤが設定したレイヤと一致するときのみコンボが成立します。各レイヤ番号と設定値の各ビットが対応します。

省略した場合は`0xffff`が適用され、すべてのレイヤでコンボが有効になります。

#### `application.leaders`

リーダーシーケンスをグループ化します

リーダーキーの詳細についてはQMKのドキュメントを参照してください。

#### `application.leaders.leader`

リーダーシーケンスを定義します。

#### `application.leaders.leader.keys`

リーダーシーケンスを実行するキーの順序を設定します。

`application.keymaps.keymap.map`で設定した置き換え後のキーで指定してください。

#### `application.leaders.leader.keycode`

リーダーシーケンスを入力したときに実行するキーコードを設定します。

動作一覧のうちタップダンス以外の動作を設定できます

#### `application.overrides`

キーオーバーライドをグループ化します

キーオーバーライドの詳細についてはQMKのドキュメントを参照してください。

#### `application.overrides.(basic|w_layer|w_layer_neg|w_layer_neg_opt)`

`application.overrides` 以下にはオーバーライドとして `basic`, `w_layer`, `w_layer_neg`, `w_layer_neg_opt` の配列を設定できます。それぞれの設定の詳細についてはQMKのドキュメントにある、`ko_make_basic`, `ko_make_with_layers`,  `ko_make_with_layer_and_negmods`, `ko_make_with_layer_and_negmods_and_options` を参照してください。


```yaml
    overrides:
      # Shift+Enterが押されたらEnterを送信する
      - basic:
          trigger_mods:
            - Shift
          trigger_key: KC_ENT 
          replacement_key: KC_ENT
      # Enterが押されたらShift+Enterを送信する
      - w_layer_neg:
          trigger_mods: []
          trigger_key: KC_ENT
          replacement_key: S(KC_ENT)
          layers: 0xffff
          negative_mask:
            - Shift
```

#### `per_key_option`

`LT()`キーなどの動作条件を設定します

#### `per_key_option.<keycode>.tapping_term`

キーごとに`TAPPING_TERM`を設定します。

省略した場合は`default.tapping_term`の値が使用されます。

#### `per_key_option.<keycode>.quick_tap_term`

キーごとに`QUICK_TAP_TERM`を設定します。

省略した場合は`default.quick_tap_term`の値が使用されます。

#### `per_key_option.<keycode>.permissive_hold`

キーごとに`PERMISSIVE_HOLD`を設定します。

省略した場合は`default.permissive_hold`の値が使用されます。

#### `per_key_option.<keycode>.hold_on_other_key_press`

キーごとに`HOLD_ON_OTHER_KEY_PRESS`を設定します。

省略した場合は`default.hold_on_other_key_press`の値が使用されます。

#### `per_key_option.<keycode>.retro_tapping`

キーごとに`RETRO_TAPPING`を設定します。

省略した場合は`default.retro_tapping`の値が使用されます。

#### `default`

`application`, `per_key_option` で省略した設定値のデフォルト値や、EEPROM初期化時の状態を設定します。

#### `default.combo_term`

`COMBO_TERM`を設定します。

#### `default.combo_press_in_order`

`COMBO_PRESS_IN_ORDER`を設定します。

#### `default.tapping_term`

`TAPPING_TERM`を設定します。

#### `default.quick_tap_term`

`QUICK_TAP_TERM`を設定します。

#### `default.permissive_hold`

`PERMISSIVE_HOLD`を設定します。

#### `default.hold_on_other_key_press`

`HOLD_ON_OTHER_KEY_PRESS`を設定します。

#### `default.retro_tapping`

`RETRO_TAPPING`を設定します。

#### `default.keyboard_language`

接続しているキーボードの言語配列を設定します (`US` or `JP`)。

省略した場合は`US`が設定されます。

注: この設定はEEPROM初期化時のデフォルト値です。EEPROM上の設定値は`SET_KB_LANG_US`, `SET_KB_LANG_JP`を押すことで切り替わります。

#### `default.os_language`

接続先OSのキーボード言語設定を設定します (`US` or `JP`)。

マクロ送信時にOS設定に合わせて送信するキーが変化します。

`default.keyboard_language`と`default.os_language`が異なる場合、KeyOverridesに自動的に差異を吸収する設定が追加されます。

省略した場合は`US`が設定されます。

注: この設定はEEPROM初期化時のデフォルト値です。EEPROM上の設定値は`SET_OS_LANG_US`, `SET_OS_LANG_JP`を押すことで切り替わります。

#### `default.mouse_gesture`

マウスジェスチャが実行するカーソル移動量の閾値を設定します。デバイスにマウスを接続している際、レイヤを移動した状態でカーソルを動かしてから元のレイヤに戻ると、カーソルの移動方向(斜め4方向)に応じた動作を実行できます。設定例についてはサンプルを参考にしてください。

省略した場合は`30`が設定されます。

### 設定可能な動作一覧

#### キーコード

QMKのキーコードをそのまま設定します。Keyboard Quantizer Configurator Generatorのエディタにはキーコードの補完機能も実装されています。

キーコードを数値で指定することもできます。数字以外の文字はそのまま入力することもできます。`"`や`\`をそのまま指定したい場合は、`\`でエスケープしてください。

例: `KC_A`, `LT(1, KC_SPC)`, `0x0004`, `4`
```yaml
# バックスラッシュ
KC_BSLS
KC_BACKSLASH
"\\"
# ダブルクオーテーション
KC_DQT
KC_DOUBLE_QUOTE
S(KC_QUT)
"\""
```

Keyboard Quantizer独自の拡張として下記が追加されています

|キーコード|説明|
|-|-|
|`LAUNCH_COMPANION`|マクロ機能とvirtser機能を使用して、PCにコンパニオンアプリを送信、実行します。具体的にはWin+X, IでPowerShellを起動し、コンパニオンアプリの受信用スクリプトをマクロで送信します。送信完了後、Enterキーを押すとスクリプトが実行され、シリアルポートを通してコンパニオンアプリを送受信し実行します|
|`SET_KB_LANG_US`|接続キーボードの配列がUS配列であるとして処理します|
|`SET_KB_LANG_JP`|接続キーボードの配列がJIS配列であるとして処理します|
|`SET_OS_LANG_US`|接続先OSのキーボード設定がUSであるとして処理します|
|`SET_OS_LANG_JP`|接続先OSのキーボード設定がJPであるとして処理します|
|`MS_GESTURE_DR`|マウスジェスチャ（右下）の設定に使用します|
|`MS_GESTURE_DL`|マウスジェスチャ（左下）の設定に使用します|
|`MS_GESTURE_UL`|マウスジェスチャ（左上）の設定に使用します|
|`MS_GESTURE_UR`|マウスジェスチャ（右上）の設定に使用します|


#### マクロ

QMKのマクロを設定します。
マクロは文字列またはアクション (down, up, tap, delay)の配列で定義します。

形式: `{ macro : [ <string> | { action: down|up|tap, keycodes:[<keycodes>] } | { action: delay, duration:<ms> }]}`

例: `{ macro: [Macro String] }`

```yaml
# Ctrl+左を入力後、macroという文字列を入力
{macro:
   [{action: down, keycodes: [KC_LCTL]},
    {action: tap, keycodes: [KC_LEFT]},
    {action: up, keycodes: [KC_LCTL]},
    macro ]}
```

#### タップダンス

シングルタップ、シングルホールド（一度目の押下で長押し）、ダブルタップ、ダブルホールド（二度目の押下で長押し）のそれぞれに動作を設定できます。

各動作にはタップダンス以外の動作（キーコード、マクロ等）を設定できます

形式: `{ tap_dance: { single_tap: <action>, single_hold: <action>, double_tap: <action>, double_hold: <action> }}`

例:
```yaml
# jを2回タップしたらESCを入力する
KC_J: { tap_dance: { single_tap: KC_J, double_tap: KC_ESC }}
```

#### コマンド

コンパニオンアプリを使用している場合に、アプリから任意のコマンドを実行します。指定された文字列をPowerShellの`Invoke-Expression`を使って実行します。使用にあたっては十分に注意してください。

形式: `{ command : <string> }`

例:
```yaml
# メモ帳を起動する
{ command: start notepad }
```

#### ユニコード文字列

コンパニオンアプリを使用している場合に、IMEを経由してユニコード文字を入力します。IME側が対応している必要があります（Microsoft IMEは対応、Google日本語入力は非対応）

形式: `{ unicode_string : <string> }`

例: `{ unicode_string: ユニコード文字列😀 }`


## 設定例

```yaml
- application:
    # 常時有効な設定
    keymaps:
      - keymap:
          layer: 0
          map:
            # CAPSを単押しTAB, 長押しCTRL
            KC_CAPS: LCTL_T(KC_TAB)
            # RSHIFTを単押しでLEADER,　長押しでSHIFT
            KC_RSFT:
              { tap_dance: { single_tap: QK_LEAD, single_hold: KC_RSFT } }
    combos:
      - combo:
          # D,L同時押しで一行削除
          keys: [KC_D, KC_L]
          keycode:
            {
              macro:
                [
                  { action: down, keycodes: [KC_LCTL] }, { action: tap, keycodes: [KC_LEFT] }, { action: down, keycodes: [KC_LSFT] },
                  { action: tap, keycodes: [KC_RGHT] }, { action: up, keycodes: [KC_LCTL, KC_LSFT] }, { action: tap, keycodes: [KC_BSPC] },
                ],
            }
          # 100ms以上長押ししたときだけ発動
          term: 100
          only: hold
    leaders:
      # LEADERのあとに入れたキーの順番で分岐
      - leader:
          # twitterを開く
          keys: [KC_T, KC_W, KC_T]
          keycode: { command:  start firefox -ArgumentList "-url https://twitter.com" }
      - leader:
          # コンパニオンアプリを送り込む
          keys: [KC_C, KC_M, KC_P]
          keycode: LAUNCH_COMPANION
- application:
    # フォーカス中の画面がchatGPTのときだけ有効なキーマップ
    url: https://chat.openai.com/.*
    overrides:
      # Shift+Enter押したらEnter, Enter押したらShift+Enterが押されるようにする
      - basic:
          trigger_mods:
            - Shift
          trigger_key: KC_ENT
          replacement_key: KC_ENT
      - w_layer_neg:
          trigger_mods: []
          trigger_key: KC_ENT
          replacement_key: S(KC_ENT)
          layers: 0xffff
          negative_mask:
            - Shift
- application:
    # Libreoffice Impressのときだけ有効
    title: ".*Impress$"
    leaders:
      - leader:
          # 上ぞろえ
          keys: [KC_A, KC_T]
          keycode: { macro: [{ action: tap, keycodes: [KC_LALT] }, ont] }
```

```yaml
# マウス用設定
- application:
    # 常時有効なキーマップを定義する
    keymaps:
      - keymap:
          # レイヤ0ではボタン6,7,8の動作を変更する
          layer: 0
          map:
            # ボタン6,7でコピペ
            KC_BTN6: LCTL(KC_C)
            KC_BTN7: LCTL(KC_V)
            # ボタン8をタップしたときは中クリック、長押ししたときはレイヤ1に移動
            KC_BTN8: LT(1, KC_BTN3)
      - keymap:
          # レイヤ1では各ボタン、ホイール、ジェスチャに機能を割り当てる
          layer: 1
          map:
            KC_BTN1: KC_ENT
            KC_BTN2: KC_BSPC
            # 中クリックで再生・停止
            KC_BTN3: KC_MEDIA_STOP
            # レイヤ1でのホイールの動作を割り当てる
            # 左右で曲送り、曲戻し
            KC_MS_WH_RIGHT: KC_MEDIA_PREV_TRACK
            KC_MS_WH_LEFT: KC_MEDIA_NEXT_TRACK
            # 上下でウィンドウ切り替え
            KC_MS_WH_UP: LALT(KC_TAB)
            KC_MS_WH_DOWN: LSA(KC_TAB)
            # レイヤ1の状態でカーソルを動かし、レイヤ0に戻るタイミングでマウスジェスチャが実行される
            # 左下に移動したらEndを送信
            MS_GESTURE_DL: KC_END
            # 左上に移動したらHomeを送信
            MS_GESTURE_UL: KC_HOME
```