# Schema Docs

- [root \> root items](#root--root-items)
  - [Property `root > root items > oneOf > Application`](#property-root--root-items--oneof--application)
  - [Property `root > root items > oneOf > PerKeyOption`](#property-root--root-items--oneof--perkeyoption)
    - [Property `root > root items > oneOf > item 1 > per_key_option`](#property-root--root-items--oneof--item-1--per_key_option)
      - [Property `root > root items > oneOf > item 1 > per_key_option > additionalProperties`](#property-root--root-items--oneof--item-1--per_key_option--additionalproperties)
      - [Property `root > root items > oneOf > item 1 > per_key_option > additionalProperties > tapping_term`](#property-root--root-items--oneof--item-1--per_key_option--additionalproperties--tapping_term)
      - [Property `root > root items > oneOf > item 1 > per_key_option > additionalProperties > quick_tap_term`](#property-root--root-items--oneof--item-1--per_key_option--additionalproperties--quick_tap_term)
      - [Property `root > root items > oneOf > item 1 > per_key_option > additionalProperties > permissive_hold`](#property-root--root-items--oneof--item-1--per_key_option--additionalproperties--permissive_hold)
      - [Property `root > root items > oneOf > item 1 > per_key_option > additionalProperties > hold_on_other_key_press`](#property-root--root-items--oneof--item-1--per_key_option--additionalproperties--hold_on_other_key_press)
      - [Property `root > root items > oneOf > item 1 > per_key_option > additionalProperties > retro_tapping`](#property-root--root-items--oneof--item-1--per_key_option--additionalproperties--retro_tapping)
  - [Property `root > root items > oneOf > DefaultValues`](#property-root--root-items--oneof--defaultvalues)
    - [Property `root > root items > oneOf > item 2 > default`](#property-root--root-items--oneof--item-2--default)
      - [Property `root > root items > oneOf > item 2 > default > combo_term`](#property-root--root-items--oneof--item-2--default--combo_term)
      - [Property `root > root items > oneOf > item 2 > default > combo_press_in_order`](#property-root--root-items--oneof--item-2--default--combo_press_in_order)
      - [Property `root > root items > oneOf > item 2 > default > tapping_term`](#property-root--root-items--oneof--item-2--default--tapping_term)
      - [Property `root > root items > oneOf > item 2 > default > quick_tap_term`](#property-root--root-items--oneof--item-2--default--quick_tap_term)
      - [Property `root > root items > oneOf > item 2 > default > permissive_hold`](#property-root--root-items--oneof--item-2--default--permissive_hold)
      - [Property `root > root items > oneOf > item 2 > default > hold_on_other_key_press`](#property-root--root-items--oneof--item-2--default--hold_on_other_key_press)
      - [Property `root > root items > oneOf > item 2 > default > retro_tapping`](#property-root--root-items--oneof--item-2--default--retro_tapping)
      - [Property `root > root items > oneOf > item 2 > default > keyboard_language`](#property-root--root-items--oneof--item-2--default--keyboard_language)
      - [Property `root > root items > oneOf > item 2 > default > os_language`](#property-root--root-items--oneof--item-2--default--os_language)
      - [Property `root > root items > oneOf > item 2 > default > mouse_gesture_threshold`](#property-root--root-items--oneof--item-2--default--mouse_gesture_threshold)
- [At least one of the items must be](#at-least-one-of-the-items-must-be)
  - [Property `root > contains > application`](#property-root--contains--application)
    - [Property `root > contains > application > title`](#property-root--contains--application--title)
    - [Property `root > contains > application > process`](#property-root--contains--application--process)
    - [Property `root > contains > application > url`](#property-root--contains--application--url)
    - [Property `root > contains > application > ime_mode`](#property-root--contains--application--ime_mode)
    - [Property `root > contains > application > ime_on`](#property-root--contains--application--ime_on)
    - [Property `root > contains > application > keymaps`](#property-root--contains--application--keymaps)
      - [root \> contains \> application \> keymaps \> Keymap](#root--contains--application--keymaps--keymap)
      - [Property `root > contains > application > keymaps > keymaps items > keymap`](#property-root--contains--application--keymaps--keymaps-items--keymap)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > layer`](#property-root--contains--application--keymaps--keymaps-items--keymap--layer)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map`](#property-root--contains--application--keymaps--keymaps-items--keymap--map)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > Action`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--action)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 0`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--item-0)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > Macro`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--macro)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 1 > macro`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--item-1--macro)
      - [root \> contains \> application \> keymaps \> keymaps items \> keymap \> map \> additionalProperties \> oneOf \> item 1 \> macro \> macro items](#root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--item-1--macro--macro-items)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 1 > macro > macro items > oneOf > item 0`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--item-1--macro--macro-items--oneof--item-0)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 1 > macro > macro items > oneOf > item 0 > action`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--item-1--macro--macro-items--oneof--item-0--action)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 1 > macro > macro items > oneOf > item 0 > keycodes`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--item-1--macro--macro-items--oneof--item-0--keycodes)
      - [root \> contains \> application \> keymaps \> keymaps items \> keymap \> map \> additionalProperties \> oneOf \> item 1 \> macro \> macro items \> oneOf \> item 0 \> keycodes \> keycodes items](#root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--item-1--macro--macro-items--oneof--item-0--keycodes--keycodes-items)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 1 > macro > macro items > oneOf > item 1`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--item-1--macro--macro-items--oneof--item-1)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 1 > macro > macro items > oneOf > item 1 > action`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--item-1--macro--macro-items--oneof--item-1--action)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 1 > macro > macro items > oneOf > item 1 > duration`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--item-1--macro--macro-items--oneof--item-1--duration)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 1 > macro > macro items > oneOf > item 2`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--item-1--macro--macro-items--oneof--item-2)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > Command`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--command)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 2 > command`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--item-2--command)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > UnicodeString`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--unicodestring)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 3 > unicode_string`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--item-3--unicode_string)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > TapDance`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--tapdance)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 4 > tap_dance`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--item-4--tap_dance)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 4 > tap_dance > single_tap`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--item-4--tap_dance--single_tap)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 4 > tap_dance > single_hold`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--item-4--tap_dance--single_hold)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 4 > tap_dance > double_tap`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--item-4--tap_dance--double_tap)
      - [Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 4 > tap_dance > double_hold`](#property-root--contains--application--keymaps--keymaps-items--keymap--map--additionalproperties--oneof--item-4--tap_dance--double_hold)
    - [Property `root > contains > application > combos`](#property-root--contains--application--combos)
      - [root \> contains \> application \> combos \> Combo](#root--contains--application--combos--combo)
      - [Property `root > contains > application > combos > combos items > combo`](#property-root--contains--application--combos--combos-items--combo)
      - [Property `root > contains > application > combos > combos items > combo > keys`](#property-root--contains--application--combos--combos-items--combo--keys)
      - [root \> contains \> application \> combos \> combos items \> combo \> keys \> keys items](#root--contains--application--combos--combos-items--combo--keys--keys-items)
      - [Property `root > contains > application > combos > combos items > combo > keycode`](#property-root--contains--application--combos--combos-items--combo--keycode)
      - [Property `root > contains > application > combos > combos items > combo > term`](#property-root--contains--application--combos--combos-items--combo--term)
      - [Property `root > contains > application > combos > combos items > combo > only`](#property-root--contains--application--combos--combos-items--combo--only)
      - [Property `root > contains > application > combos > combos items > combo > press_in_order`](#property-root--contains--application--combos--combos-items--combo--press_in_order)
      - [Property `root > contains > application > combos > combos items > combo > layer`](#property-root--contains--application--combos--combos-items--combo--layer)
    - [Property `root > contains > application > leaders`](#property-root--contains--application--leaders)
      - [root \> contains \> application \> leaders \> Leader](#root--contains--application--leaders--leader)
      - [Property `root > contains > application > leaders > leaders items > leader`](#property-root--contains--application--leaders--leaders-items--leader)
      - [Property `root > contains > application > leaders > leaders items > leader > keys`](#property-root--contains--application--leaders--leaders-items--leader--keys)
      - [root \> contains \> application \> leaders \> leaders items \> leader \> keys \> keys items](#root--contains--application--leaders--leaders-items--leader--keys--keys-items)
      - [Property `root > contains > application > leaders > leaders items > leader > keycode`](#property-root--contains--application--leaders--leaders-items--leader--keycode)
    - [Property `root > contains > application > overrides`](#property-root--contains--application--overrides)
      - [root \> contains \> application \> overrides \> KeyOverride](#root--contains--application--overrides--keyoverride)
      - [Property `root > contains > application > overrides > overrides items > oneOf > basic`](#property-root--contains--application--overrides--overrides-items--oneof--basic)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 0 > basic`](#property-root--contains--application--overrides--overrides-items--oneof--item-0--basic)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 0 > basic > trigger_mods`](#property-root--contains--application--overrides--overrides-items--oneof--item-0--basic--trigger_mods)
      - [root \> contains \> application \> overrides \> overrides items \> oneOf \> item 0 \> basic \> trigger\_mods \> trigger\_mods items](#root--contains--application--overrides--overrides-items--oneof--item-0--basic--trigger_mods--trigger_mods-items)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 0 > basic > trigger_key`](#property-root--contains--application--overrides--overrides-items--oneof--item-0--basic--trigger_key)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 0 > basic > replacement_key`](#property-root--contains--application--overrides--overrides-items--oneof--item-0--basic--replacement_key)
      - [Property `root > contains > application > overrides > overrides items > oneOf > w_layer`](#property-root--contains--application--overrides--overrides-items--oneof--w_layer)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 1 > w_layer`](#property-root--contains--application--overrides--overrides-items--oneof--item-1--w_layer)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 1 > w_layer > trigger_mods`](#property-root--contains--application--overrides--overrides-items--oneof--item-1--w_layer--trigger_mods)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 1 > w_layer > trigger_key`](#property-root--contains--application--overrides--overrides-items--oneof--item-1--w_layer--trigger_key)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 1 > w_layer > replacement_key`](#property-root--contains--application--overrides--overrides-items--oneof--item-1--w_layer--replacement_key)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 1 > w_layer > layers`](#property-root--contains--application--overrides--overrides-items--oneof--item-1--w_layer--layers)
      - [Property `root > contains > application > overrides > overrides items > oneOf > w_layer_neg`](#property-root--contains--application--overrides--overrides-items--oneof--w_layer_neg)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 2 > w_layer_neg`](#property-root--contains--application--overrides--overrides-items--oneof--item-2--w_layer_neg)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 2 > w_layer_neg > trigger_mods`](#property-root--contains--application--overrides--overrides-items--oneof--item-2--w_layer_neg--trigger_mods)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 2 > w_layer_neg > trigger_key`](#property-root--contains--application--overrides--overrides-items--oneof--item-2--w_layer_neg--trigger_key)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 2 > w_layer_neg > replacement_key`](#property-root--contains--application--overrides--overrides-items--oneof--item-2--w_layer_neg--replacement_key)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 2 > w_layer_neg > layers`](#property-root--contains--application--overrides--overrides-items--oneof--item-2--w_layer_neg--layers)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 2 > w_layer_neg > negative_mask`](#property-root--contains--application--overrides--overrides-items--oneof--item-2--w_layer_neg--negative_mask)
      - [Property `root > contains > application > overrides > overrides items > oneOf > w_layer_neg_opt`](#property-root--contains--application--overrides--overrides-items--oneof--w_layer_neg_opt)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 3 > w_layer_neg_opt`](#property-root--contains--application--overrides--overrides-items--oneof--item-3--w_layer_neg_opt)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 3 > w_layer_neg_opt > trigger_mods`](#property-root--contains--application--overrides--overrides-items--oneof--item-3--w_layer_neg_opt--trigger_mods)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 3 > w_layer_neg_opt > trigger_key`](#property-root--contains--application--overrides--overrides-items--oneof--item-3--w_layer_neg_opt--trigger_key)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 3 > w_layer_neg_opt > replacement_key`](#property-root--contains--application--overrides--overrides-items--oneof--item-3--w_layer_neg_opt--replacement_key)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 3 > w_layer_neg_opt > layers`](#property-root--contains--application--overrides--overrides-items--oneof--item-3--w_layer_neg_opt--layers)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 3 > w_layer_neg_opt > negative_mask`](#property-root--contains--application--overrides--overrides-items--oneof--item-3--w_layer_neg_opt--negative_mask)
      - [Property `root > contains > application > overrides > overrides items > oneOf > item 3 > w_layer_neg_opt > options`](#property-root--contains--application--overrides--overrides-items--oneof--item-3--w_layer_neg_opt--options)
      - [root \> contains \> application \> overrides \> overrides items \> oneOf \> item 3 \> w\_layer\_neg\_opt \> options \> options items](#root--contains--application--overrides--overrides-items--oneof--item-3--w_layer_neg_opt--options--options-items)

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [root items](#items)            | -           |

## <a name="autogenerated_heading_2"></a>root > root items

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| One of(Option)                   |
| -------------------------------- |
| [Application](#items_oneOf_i0)   |
| [PerKeyOption](#items_oneOf_i1)  |
| [DefaultValues](#items_oneOf_i2) |

### <a name="items_oneOf_i0"></a>Property `root > root items > oneOf > Application`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [contains](#contains)                                                     |

### <a name="items_oneOf_i1"></a>Property `root > root items > oneOf > PerKeyOption`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/PerKeyOption                                                |

| Property                                            | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [per_key_option](#items_oneOf_i1_per_key_option ) | No      | object | No         | -          | -                 |

#### <a name="items_oneOf_i1_per_key_option"></a>Property `root > root items > oneOf > item 1 > per_key_option`

|                           |                                                                                                                                         |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                |
| **Required**              | Yes                                                                                                                                     |
| **Additional properties** | [[Should-conform]](#items_oneOf_i1_per_key_option_additionalProperties "Each additional property must conform to the following schema") |

| Property                                                   | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [](#items_oneOf_i1_per_key_option_additionalProperties ) | No      | object | No         | -          | -                 |

##### <a name="items_oneOf_i1_per_key_option_additionalProperties"></a>Property `root > root items > oneOf > item 1 > per_key_option > additionalProperties`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                                                                                                  | Pattern | Type    | Deprecated | Definition | Title/Description |
| --------------------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [tapping_term](#items_oneOf_i1_per_key_option_additionalProperties_tapping_term )                       | No      | integer | No         | -          | -                 |
| - [quick_tap_term](#items_oneOf_i1_per_key_option_additionalProperties_quick_tap_term )                   | No      | integer | No         | -          | -                 |
| - [permissive_hold](#items_oneOf_i1_per_key_option_additionalProperties_permissive_hold )                 | No      | boolean | No         | -          | -                 |
| - [hold_on_other_key_press](#items_oneOf_i1_per_key_option_additionalProperties_hold_on_other_key_press ) | No      | boolean | No         | -          | -                 |
| - [retro_tapping](#items_oneOf_i1_per_key_option_additionalProperties_retro_tapping )                     | No      | boolean | No         | -          | -                 |

##### <a name="items_oneOf_i1_per_key_option_additionalProperties_tapping_term"></a>Property `root > root items > oneOf > item 1 > per_key_option > additionalProperties > tapping_term`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

##### <a name="items_oneOf_i1_per_key_option_additionalProperties_quick_tap_term"></a>Property `root > root items > oneOf > item 1 > per_key_option > additionalProperties > quick_tap_term`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

##### <a name="items_oneOf_i1_per_key_option_additionalProperties_permissive_hold"></a>Property `root > root items > oneOf > item 1 > per_key_option > additionalProperties > permissive_hold`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

##### <a name="items_oneOf_i1_per_key_option_additionalProperties_hold_on_other_key_press"></a>Property `root > root items > oneOf > item 1 > per_key_option > additionalProperties > hold_on_other_key_press`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

##### <a name="items_oneOf_i1_per_key_option_additionalProperties_retro_tapping"></a>Property `root > root items > oneOf > item 1 > per_key_option > additionalProperties > retro_tapping`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

### <a name="items_oneOf_i2"></a>Property `root > root items > oneOf > DefaultValues`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/DefaultValues                                               |

| Property                              | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [default](#items_oneOf_i2_default ) | No      | object | No         | -          | -                 |

#### <a name="items_oneOf_i2_default"></a>Property `root > root items > oneOf > item 2 > default`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | Yes                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                                                                      | Pattern | Type             | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| - [combo_term](#items_oneOf_i2_default_combo_term )                           | No      | integer          | No         | -          | -                 |
| - [combo_press_in_order](#items_oneOf_i2_default_combo_press_in_order )       | No      | boolean          | No         | -          | -                 |
| - [tapping_term](#items_oneOf_i2_default_tapping_term )                       | No      | integer          | No         | -          | -                 |
| - [quick_tap_term](#items_oneOf_i2_default_quick_tap_term )                   | No      | integer          | No         | -          | -                 |
| - [permissive_hold](#items_oneOf_i2_default_permissive_hold )                 | No      | boolean          | No         | -          | -                 |
| - [hold_on_other_key_press](#items_oneOf_i2_default_hold_on_other_key_press ) | No      | boolean          | No         | -          | -                 |
| - [retro_tapping](#items_oneOf_i2_default_retro_tapping )                     | No      | boolean          | No         | -          | -                 |
| - [keyboard_language](#items_oneOf_i2_default_keyboard_language )             | No      | enum (of string) | No         | -          | -                 |
| - [os_language](#items_oneOf_i2_default_os_language )                         | No      | enum (of string) | No         | -          | -                 |
| - [mouse_gesture_threshold](#items_oneOf_i2_default_mouse_gesture_threshold ) | No      | integer          | No         | -          | -                 |

##### <a name="items_oneOf_i2_default_combo_term"></a>Property `root > root items > oneOf > item 2 > default > combo_term`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

##### <a name="items_oneOf_i2_default_combo_press_in_order"></a>Property `root > root items > oneOf > item 2 > default > combo_press_in_order`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

##### <a name="items_oneOf_i2_default_tapping_term"></a>Property `root > root items > oneOf > item 2 > default > tapping_term`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

##### <a name="items_oneOf_i2_default_quick_tap_term"></a>Property `root > root items > oneOf > item 2 > default > quick_tap_term`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

##### <a name="items_oneOf_i2_default_permissive_hold"></a>Property `root > root items > oneOf > item 2 > default > permissive_hold`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

##### <a name="items_oneOf_i2_default_hold_on_other_key_press"></a>Property `root > root items > oneOf > item 2 > default > hold_on_other_key_press`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

##### <a name="items_oneOf_i2_default_retro_tapping"></a>Property `root > root items > oneOf > item 2 > default > retro_tapping`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

##### <a name="items_oneOf_i2_default_keyboard_language"></a>Property `root > root items > oneOf > item 2 > default > keyboard_language`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

Must be one of:
* "US"
* "JP"

##### <a name="items_oneOf_i2_default_os_language"></a>Property `root > root items > oneOf > item 2 > default > os_language`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

Must be one of:
* "US"
* "JP"

##### <a name="items_oneOf_i2_default_mouse_gesture_threshold"></a>Property `root > root items > oneOf > item 2 > default > mouse_gesture_threshold`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

## <a name="autogenerated_heading_3"></a>At least one of the items must be

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/Application                                                 |

| Property                                | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [application](#contains_application ) | No      | object | No         | -          | -                 |

### <a name="contains_application"></a>Property `root > contains > application`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | Yes                                                     |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

| Property                                        | Pattern | Type    | Deprecated | Definition | Title/Description |
| ----------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [title](#contains_application_title )         | No      | string  | No         | -          | -                 |
| - [process](#contains_application_process )     | No      | string  | No         | -          | -                 |
| - [url](#contains_application_url )             | No      | string  | No         | -          | -                 |
| - [ime_mode](#contains_application_ime_mode )   | No      | integer | No         | -          | -                 |
| - [ime_on](#contains_application_ime_on )       | No      | integer | No         | -          | -                 |
| - [keymaps](#contains_application_keymaps )     | No      | array   | No         | -          | -                 |
| - [combos](#contains_application_combos )       | No      | array   | No         | -          | -                 |
| - [leaders](#contains_application_leaders )     | No      | array   | No         | -          | -                 |
| - [overrides](#contains_application_overrides ) | No      | array   | No         | -          | -                 |

#### <a name="contains_application_title"></a>Property `root > contains > application > title`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="contains_application_process"></a>Property `root > contains > application > process`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="contains_application_url"></a>Property `root > contains > application > url`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="contains_application_ime_mode"></a>Property `root > contains > application > ime_mode`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

#### <a name="contains_application_ime_on"></a>Property `root > contains > application > ime_on`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

#### <a name="contains_application_keymaps"></a>Property `root > contains > application > keymaps`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be               | Description |
| --------------------------------------------- | ----------- |
| [Keymap](#contains_application_keymaps_items) | -           |

##### <a name="autogenerated_heading_4"></a>root > contains > application > keymaps > Keymap

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/Keymap                                                      |

| Property                                                | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [keymap](#contains_application_keymaps_items_keymap ) | No      | object | No         | -          | -                 |

##### <a name="contains_application_keymaps_items_keymap"></a>Property `root > contains > application > keymaps > keymaps items > keymap`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | Yes                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                                                     | Pattern | Type    | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------ | ------- | ------- | ---------- | ---------- | ----------------- |
| + [layer](#contains_application_keymaps_items_keymap_layer ) | No      | integer | No         | -          | -                 |
| + [map](#contains_application_keymaps_items_keymap_map )     | No      | object  | No         | -          | -                 |

##### <a name="contains_application_keymaps_items_keymap_layer"></a>Property `root > contains > application > keymaps > keymaps items > keymap > layer`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

##### <a name="contains_application_keymaps_items_keymap_map"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map`

|                           |                                                                                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                |
| **Required**              | Yes                                                                                                                                                     |
| **Additional properties** | [[Should-conform]](#contains_application_keymaps_items_keymap_map_additionalProperties "Each additional property must conform to the following schema") |

| Property                                                                   | Pattern | Type   | Deprecated | Definition              | Title/Description |
| -------------------------------------------------------------------------- | ------- | ------ | ---------- | ----------------------- | ----------------- |
| - [](#contains_application_keymaps_items_keymap_map_additionalProperties ) | No      | object | No         | In #/definitions/Action | -                 |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > Action`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/Action                                                      |

| One of(Option)                                                                                |
| --------------------------------------------------------------------------------------------- |
| [item 0](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i0)        |
| [Macro](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1)         |
| [Command](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i2)       |
| [UnicodeString](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i3) |
| [TapDance](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i4)      |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i0"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > Macro`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
| **Defined in**            | #/definitions/Macro                                     |

| Property                                                                                       | Pattern | Type  | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------------------------------- | ------- | ----- | ---------- | ---------- | ----------------- |
| + [macro](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1_macro ) | No      | array | No         | -          | -                 |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1_macro"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 1 > macro`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | Yes     |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                                         | Description |
| ------------------------------------------------------------------------------------------------------- | ----------- |
| [macro items](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1_macro_items) | -           |

##### <a name="autogenerated_heading_5"></a>root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 1 > macro > macro items

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| One of(Option)                                                                                              |
| ----------------------------------------------------------------------------------------------------------- |
| [item 0](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1_macro_items_oneOf_i0) |
| [item 1](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1_macro_items_oneOf_i1) |
| [item 2](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1_macro_items_oneOf_i2) |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1_macro_items_oneOf_i0"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 1 > macro > macro items > oneOf > item 0`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

| Property                                                                                                                  | Pattern | Type             | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| + [action](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1_macro_items_oneOf_i0_action )     | No      | enum (of string) | No         | -          | -                 |
| + [keycodes](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1_macro_items_oneOf_i0_keycodes ) | No      | array of string  | No         | -          | -                 |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1_macro_items_oneOf_i0_action"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 1 > macro > macro items > oneOf > item 0 > action`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

Must be one of:
* "tap"
* "down"
* "up"

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1_macro_items_oneOf_i0_keycodes"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 1 > macro > macro items > oneOf > item 0 > keycodes`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | Yes               |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                                                                    | Description |
| ---------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [keycodes items](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1_macro_items_oneOf_i0_keycodes_items) | -           |

##### <a name="autogenerated_heading_6"></a>root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 1 > macro > macro items > oneOf > item 0 > keycodes > keycodes items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1_macro_items_oneOf_i1"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 1 > macro > macro items > oneOf > item 1`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

| Property                                                                                                                  | Pattern | Type    | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| + [action](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1_macro_items_oneOf_i1_action )     | No      | const   | No         | -          | -                 |
| + [duration](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1_macro_items_oneOf_i1_duration ) | No      | integer | No         | -          | -                 |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1_macro_items_oneOf_i1_action"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 1 > macro > macro items > oneOf > item 1 > action`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

Specific value: `"delay"`

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1_macro_items_oneOf_i1_duration"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 1 > macro > macro items > oneOf > item 1 > duration`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i1_macro_items_oneOf_i2"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 1 > macro > macro items > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i2"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > Command`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
| **Defined in**            | #/definitions/Command                                   |

| Property                                                                                           | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [command](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i2_command ) | No      | string | No         | -          | -                 |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i2_command"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 2 > command`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i3"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > UnicodeString`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
| **Defined in**            | #/definitions/UnicodeString                             |

| Property                                                                                                         | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [unicode_string](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i3_unicode_string ) | No      | string | No         | -          | -                 |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i3_unicode_string"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 3 > unicode_string`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i4"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > TapDance`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/TapDance                                                    |

| Property                                                                                               | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| + [tap_dance](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i4_tap_dance ) | No      | object | No         | -          | -                 |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i4_tap_dance"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 4 > tap_dance`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | Yes                                                     |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

| Property                                                                                                             | Pattern | Type   | Deprecated | Definition                                                                                                                                         | Title/Description |
| -------------------------------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| - [single_tap](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i4_tap_dance_single_tap )   | No      | object | No         | Same as [contains_application_keymaps_items_keymap_map_additionalProperties](#contains_application_keymaps_items_keymap_map_additionalProperties ) | -                 |
| - [single_hold](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i4_tap_dance_single_hold ) | No      | object | No         | Same as [contains_application_keymaps_items_keymap_map_additionalProperties](#contains_application_keymaps_items_keymap_map_additionalProperties ) | -                 |
| - [double_tap](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i4_tap_dance_double_tap )   | No      | object | No         | Same as [contains_application_keymaps_items_keymap_map_additionalProperties](#contains_application_keymaps_items_keymap_map_additionalProperties ) | -                 |
| - [double_hold](#contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i4_tap_dance_double_hold ) | No      | object | No         | Same as [contains_application_keymaps_items_keymap_map_additionalProperties](#contains_application_keymaps_items_keymap_map_additionalProperties ) | -                 |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i4_tap_dance_single_tap"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 4 > tap_dance > single_tap`

|                           |                                                                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                                                                               |
| **Required**              | No                                                                                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.")                                                                 |
| **Same definition as**    | [contains_application_keymaps_items_keymap_map_additionalProperties](#contains_application_keymaps_items_keymap_map_additionalProperties) |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i4_tap_dance_single_hold"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 4 > tap_dance > single_hold`

|                           |                                                                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                                                                               |
| **Required**              | No                                                                                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.")                                                                 |
| **Same definition as**    | [contains_application_keymaps_items_keymap_map_additionalProperties](#contains_application_keymaps_items_keymap_map_additionalProperties) |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i4_tap_dance_double_tap"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 4 > tap_dance > double_tap`

|                           |                                                                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                                                                               |
| **Required**              | No                                                                                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.")                                                                 |
| **Same definition as**    | [contains_application_keymaps_items_keymap_map_additionalProperties](#contains_application_keymaps_items_keymap_map_additionalProperties) |

##### <a name="contains_application_keymaps_items_keymap_map_additionalProperties_oneOf_i4_tap_dance_double_hold"></a>Property `root > contains > application > keymaps > keymaps items > keymap > map > additionalProperties > oneOf > item 4 > tap_dance > double_hold`

|                           |                                                                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                                                                               |
| **Required**              | No                                                                                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.")                                                                 |
| **Same definition as**    | [contains_application_keymaps_items_keymap_map_additionalProperties](#contains_application_keymaps_items_keymap_map_additionalProperties) |

#### <a name="contains_application_combos"></a>Property `root > contains > application > combos`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [Combo](#contains_application_combos_items) | -           |

##### <a name="autogenerated_heading_7"></a>root > contains > application > combos > Combo

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/Combo                                                       |

| Property                                             | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [combo](#contains_application_combos_items_combo ) | No      | object | No         | -          | -                 |

##### <a name="contains_application_combos_items_combo"></a>Property `root > contains > application > combos > combos items > combo`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | Yes                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                                                                     | Pattern | Type             | Deprecated | Definition                                                                                                                                         | Title/Description |
| ---------------------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| + [keys](#contains_application_combos_items_combo_keys )                     | No      | array of string  | No         | -                                                                                                                                                  | -                 |
| + [keycode](#contains_application_combos_items_combo_keycode )               | No      | object           | No         | Same as [contains_application_keymaps_items_keymap_map_additionalProperties](#contains_application_keymaps_items_keymap_map_additionalProperties ) | -                 |
| - [term](#contains_application_combos_items_combo_term )                     | No      | integer          | No         | -                                                                                                                                                  | -                 |
| - [only](#contains_application_combos_items_combo_only )                     | No      | enum (of string) | No         | -                                                                                                                                                  | -                 |
| - [press_in_order](#contains_application_combos_items_combo_press_in_order ) | No      | boolean          | No         | -                                                                                                                                                  | -                 |
| - [layer](#contains_application_combos_items_combo_layer )                   | No      | integer          | No         | -                                                                                                                                                  | -                 |

##### <a name="contains_application_combos_items_combo_keys"></a>Property `root > contains > application > combos > combos items > combo > keys`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | Yes               |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                   | Description |
| ----------------------------------------------------------------- | ----------- |
| [keys items](#contains_application_combos_items_combo_keys_items) | -           |

##### <a name="autogenerated_heading_8"></a>root > contains > application > combos > combos items > combo > keys > keys items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

##### <a name="contains_application_combos_items_combo_keycode"></a>Property `root > contains > application > combos > combos items > combo > keycode`

|                           |                                                                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                                                                               |
| **Required**              | Yes                                                                                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.")                                                                 |
| **Same definition as**    | [contains_application_keymaps_items_keymap_map_additionalProperties](#contains_application_keymaps_items_keymap_map_additionalProperties) |

##### <a name="contains_application_combos_items_combo_term"></a>Property `root > contains > application > combos > combos items > combo > term`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

##### <a name="contains_application_combos_items_combo_only"></a>Property `root > contains > application > combos > combos items > combo > only`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

Must be one of:
* "None"
* "Tap"
* "Hold"
* "none"
* "tap"
* "hold"

##### <a name="contains_application_combos_items_combo_press_in_order"></a>Property `root > contains > application > combos > combos items > combo > press_in_order`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

##### <a name="contains_application_combos_items_combo_layer"></a>Property `root > contains > application > combos > combos items > combo > layer`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

#### <a name="contains_application_leaders"></a>Property `root > contains > application > leaders`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be               | Description |
| --------------------------------------------- | ----------- |
| [Leader](#contains_application_leaders_items) | -           |

##### <a name="autogenerated_heading_9"></a>root > contains > application > leaders > Leader

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/Leader                                                      |

| Property                                                | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [leader](#contains_application_leaders_items_leader ) | No      | object | No         | -          | -                 |

##### <a name="contains_application_leaders_items_leader"></a>Property `root > contains > application > leaders > leaders items > leader`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | Yes                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                                                         | Pattern | Type            | Deprecated | Definition                                                                                                                                         | Title/Description |
| ---------------------------------------------------------------- | ------- | --------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| + [keys](#contains_application_leaders_items_leader_keys )       | No      | array of string | No         | -                                                                                                                                                  | -                 |
| + [keycode](#contains_application_leaders_items_leader_keycode ) | No      | object          | No         | Same as [contains_application_keymaps_items_keymap_map_additionalProperties](#contains_application_keymaps_items_keymap_map_additionalProperties ) | -                 |

##### <a name="contains_application_leaders_items_leader_keys"></a>Property `root > contains > application > leaders > leaders items > leader > keys`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | Yes               |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                     | Description |
| ------------------------------------------------------------------- | ----------- |
| [keys items](#contains_application_leaders_items_leader_keys_items) | -           |

##### <a name="autogenerated_heading_10"></a>root > contains > application > leaders > leaders items > leader > keys > keys items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

##### <a name="contains_application_leaders_items_leader_keycode"></a>Property `root > contains > application > leaders > leaders items > leader > keycode`

|                           |                                                                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                                                                               |
| **Required**              | Yes                                                                                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.")                                                                 |
| **Same definition as**    | [contains_application_keymaps_items_keymap_map_additionalProperties](#contains_application_keymaps_items_keymap_map_additionalProperties) |

#### <a name="contains_application_overrides"></a>Property `root > contains > application > overrides`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                      | Description |
| ---------------------------------------------------- | ----------- |
| [KeyOverride](#contains_application_overrides_items) | -           |

##### <a name="autogenerated_heading_11"></a>root > contains > application > overrides > KeyOverride

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/KeyOverride                                                 |

| One of(Option)                                                    |
| ----------------------------------------------------------------- |
| [basic](#contains_application_overrides_items_oneOf_i0)           |
| [w_layer](#contains_application_overrides_items_oneOf_i1)         |
| [w_layer_neg](#contains_application_overrides_items_oneOf_i2)     |
| [w_layer_neg_opt](#contains_application_overrides_items_oneOf_i3) |

##### <a name="contains_application_overrides_items_oneOf_i0"></a>Property `root > contains > application > overrides > overrides items > oneOf > basic`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/KeyOverride/basic                                           |

| Property                                                         | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [basic](#contains_application_overrides_items_oneOf_i0_basic ) | No      | object | No         | -          | -                 |

##### <a name="contains_application_overrides_items_oneOf_i0_basic"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 0 > basic`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | Yes                                                     |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

| Property                                                                                   | Pattern | Type                      | Deprecated | Definition                               | Title/Description |
| ------------------------------------------------------------------------------------------ | ------- | ------------------------- | ---------- | ---------------------------------------- | ----------------- |
| + [trigger_mods](#contains_application_overrides_items_oneOf_i0_basic_trigger_mods )       | No      | array of enum (of string) | No         | In #/definitions/KeyOverride/modMaskType | -                 |
| + [trigger_key](#contains_application_overrides_items_oneOf_i0_basic_trigger_key )         | No      | string                    | No         | -                                        | -                 |
| + [replacement_key](#contains_application_overrides_items_oneOf_i0_basic_replacement_key ) | No      | string                    | No         | -                                        | -                 |

##### <a name="contains_application_overrides_items_oneOf_i0_basic_trigger_mods"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 0 > basic > trigger_mods`

|                |                                       |
| -------------- | ------------------------------------- |
| **Type**       | `array of enum (of string)`           |
| **Required**   | Yes                                   |
| **Defined in** | #/definitions/KeyOverride/modMaskType |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                               | Description |
| --------------------------------------------------------------------------------------------- | ----------- |
| [trigger_mods items](#contains_application_overrides_items_oneOf_i0_basic_trigger_mods_items) | -           |

##### <a name="autogenerated_heading_12"></a>root > contains > application > overrides > overrides items > oneOf > item 0 > basic > trigger_mods > trigger_mods items

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

Must be one of:
* "Shift"
* "Alt"
* "Ctrl"
* "Gui"

##### <a name="contains_application_overrides_items_oneOf_i0_basic_trigger_key"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 0 > basic > trigger_key`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

##### <a name="contains_application_overrides_items_oneOf_i0_basic_replacement_key"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 0 > basic > replacement_key`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

##### <a name="contains_application_overrides_items_oneOf_i1"></a>Property `root > contains > application > overrides > overrides items > oneOf > w_layer`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/KeyOverride/w_layer                                         |

| Property                                                             | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [w_layer](#contains_application_overrides_items_oneOf_i1_w_layer ) | No      | object | No         | -          | -                 |

##### <a name="contains_application_overrides_items_oneOf_i1_w_layer"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 1 > w_layer`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | Yes                                                     |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

| Property                                                                                     | Pattern | Type                      | Deprecated | Definition                                                                                 | Title/Description |
| -------------------------------------------------------------------------------------------- | ------- | ------------------------- | ---------- | ------------------------------------------------------------------------------------------ | ----------------- |
| + [trigger_mods](#contains_application_overrides_items_oneOf_i1_w_layer_trigger_mods )       | No      | array of enum (of string) | No         | Same as [trigger_mods](#contains_application_overrides_items_oneOf_i0_basic_trigger_mods ) | -                 |
| + [trigger_key](#contains_application_overrides_items_oneOf_i1_w_layer_trigger_key )         | No      | string                    | No         | -                                                                                          | -                 |
| + [replacement_key](#contains_application_overrides_items_oneOf_i1_w_layer_replacement_key ) | No      | string                    | No         | -                                                                                          | -                 |
| + [layers](#contains_application_overrides_items_oneOf_i1_w_layer_layers )                   | No      | integer                   | No         | -                                                                                          | -                 |

##### <a name="contains_application_overrides_items_oneOf_i1_w_layer_trigger_mods"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 1 > w_layer > trigger_mods`

|                        |                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------- |
| **Type**               | `array of enum (of string)`                                                       |
| **Required**           | Yes                                                                               |
| **Same definition as** | [trigger_mods](#contains_application_overrides_items_oneOf_i0_basic_trigger_mods) |

##### <a name="contains_application_overrides_items_oneOf_i1_w_layer_trigger_key"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 1 > w_layer > trigger_key`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

##### <a name="contains_application_overrides_items_oneOf_i1_w_layer_replacement_key"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 1 > w_layer > replacement_key`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

##### <a name="contains_application_overrides_items_oneOf_i1_w_layer_layers"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 1 > w_layer > layers`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

##### <a name="contains_application_overrides_items_oneOf_i2"></a>Property `root > contains > application > overrides > overrides items > oneOf > w_layer_neg`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/KeyOverride/w_layer_neg                                     |

| Property                                                                     | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [w_layer_neg](#contains_application_overrides_items_oneOf_i2_w_layer_neg ) | No      | object | No         | -          | -                 |

##### <a name="contains_application_overrides_items_oneOf_i2_w_layer_neg"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 2 > w_layer_neg`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | Yes                                                     |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

| Property                                                                                         | Pattern | Type                      | Deprecated | Definition                                                                                 | Title/Description |
| ------------------------------------------------------------------------------------------------ | ------- | ------------------------- | ---------- | ------------------------------------------------------------------------------------------ | ----------------- |
| + [trigger_mods](#contains_application_overrides_items_oneOf_i2_w_layer_neg_trigger_mods )       | No      | array of enum (of string) | No         | Same as [trigger_mods](#contains_application_overrides_items_oneOf_i0_basic_trigger_mods ) | -                 |
| + [trigger_key](#contains_application_overrides_items_oneOf_i2_w_layer_neg_trigger_key )         | No      | string                    | No         | -                                                                                          | -                 |
| + [replacement_key](#contains_application_overrides_items_oneOf_i2_w_layer_neg_replacement_key ) | No      | string                    | No         | -                                                                                          | -                 |
| + [layers](#contains_application_overrides_items_oneOf_i2_w_layer_neg_layers )                   | No      | integer                   | No         | -                                                                                          | -                 |
| + [negative_mask](#contains_application_overrides_items_oneOf_i2_w_layer_neg_negative_mask )     | No      | array of enum (of string) | No         | Same as [trigger_mods](#contains_application_overrides_items_oneOf_i0_basic_trigger_mods ) | -                 |

##### <a name="contains_application_overrides_items_oneOf_i2_w_layer_neg_trigger_mods"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 2 > w_layer_neg > trigger_mods`

|                        |                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------- |
| **Type**               | `array of enum (of string)`                                                       |
| **Required**           | Yes                                                                               |
| **Same definition as** | [trigger_mods](#contains_application_overrides_items_oneOf_i0_basic_trigger_mods) |

##### <a name="contains_application_overrides_items_oneOf_i2_w_layer_neg_trigger_key"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 2 > w_layer_neg > trigger_key`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

##### <a name="contains_application_overrides_items_oneOf_i2_w_layer_neg_replacement_key"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 2 > w_layer_neg > replacement_key`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

##### <a name="contains_application_overrides_items_oneOf_i2_w_layer_neg_layers"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 2 > w_layer_neg > layers`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

##### <a name="contains_application_overrides_items_oneOf_i2_w_layer_neg_negative_mask"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 2 > w_layer_neg > negative_mask`

|                        |                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------- |
| **Type**               | `array of enum (of string)`                                                       |
| **Required**           | Yes                                                                               |
| **Same definition as** | [trigger_mods](#contains_application_overrides_items_oneOf_i0_basic_trigger_mods) |

##### <a name="contains_application_overrides_items_oneOf_i3"></a>Property `root > contains > application > overrides > overrides items > oneOf > w_layer_neg_opt`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/KeyOverride/w_layer_neg_opt                                 |

| Property                                                                             | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| + [w_layer_neg_opt](#contains_application_overrides_items_oneOf_i3_w_layer_neg_opt ) | No      | object | No         | -          | -                 |

##### <a name="contains_application_overrides_items_oneOf_i3_w_layer_neg_opt"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 3 > w_layer_neg_opt`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | Yes                                                     |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

| Property                                                                                             | Pattern | Type                      | Deprecated | Definition                                                                                 | Title/Description |
| ---------------------------------------------------------------------------------------------------- | ------- | ------------------------- | ---------- | ------------------------------------------------------------------------------------------ | ----------------- |
| + [trigger_mods](#contains_application_overrides_items_oneOf_i3_w_layer_neg_opt_trigger_mods )       | No      | array of enum (of string) | No         | Same as [trigger_mods](#contains_application_overrides_items_oneOf_i0_basic_trigger_mods ) | -                 |
| + [trigger_key](#contains_application_overrides_items_oneOf_i3_w_layer_neg_opt_trigger_key )         | No      | string                    | No         | -                                                                                          | -                 |
| + [replacement_key](#contains_application_overrides_items_oneOf_i3_w_layer_neg_opt_replacement_key ) | No      | string                    | No         | -                                                                                          | -                 |
| + [layers](#contains_application_overrides_items_oneOf_i3_w_layer_neg_opt_layers )                   | No      | integer                   | No         | -                                                                                          | -                 |
| + [negative_mask](#contains_application_overrides_items_oneOf_i3_w_layer_neg_opt_negative_mask )     | No      | array of enum (of string) | No         | Same as [trigger_mods](#contains_application_overrides_items_oneOf_i0_basic_trigger_mods ) | -                 |
| + [options](#contains_application_overrides_items_oneOf_i3_w_layer_neg_opt_options )                 | No      | array of enum (of string) | No         | -                                                                                          | -                 |

##### <a name="contains_application_overrides_items_oneOf_i3_w_layer_neg_opt_trigger_mods"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 3 > w_layer_neg_opt > trigger_mods`

|                        |                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------- |
| **Type**               | `array of enum (of string)`                                                       |
| **Required**           | Yes                                                                               |
| **Same definition as** | [trigger_mods](#contains_application_overrides_items_oneOf_i0_basic_trigger_mods) |

##### <a name="contains_application_overrides_items_oneOf_i3_w_layer_neg_opt_trigger_key"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 3 > w_layer_neg_opt > trigger_key`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

##### <a name="contains_application_overrides_items_oneOf_i3_w_layer_neg_opt_replacement_key"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 3 > w_layer_neg_opt > replacement_key`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

##### <a name="contains_application_overrides_items_oneOf_i3_w_layer_neg_opt_layers"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 3 > w_layer_neg_opt > layers`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

##### <a name="contains_application_overrides_items_oneOf_i3_w_layer_neg_opt_negative_mask"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 3 > w_layer_neg_opt > negative_mask`

|                        |                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------- |
| **Type**               | `array of enum (of string)`                                                       |
| **Required**           | Yes                                                                               |
| **Same definition as** | [trigger_mods](#contains_application_overrides_items_oneOf_i0_basic_trigger_mods) |

##### <a name="contains_application_overrides_items_oneOf_i3_w_layer_neg_opt_options"></a>Property `root > contains > application > overrides > overrides items > oneOf > item 3 > w_layer_neg_opt > options`

|              |                             |
| ------------ | --------------------------- |
| **Type**     | `array of enum (of string)` |
| **Required** | Yes                         |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                               | Description |
| --------------------------------------------------------------------------------------------- | ----------- |
| [options items](#contains_application_overrides_items_oneOf_i3_w_layer_neg_opt_options_items) | -           |

##### <a name="autogenerated_heading_13"></a>root > contains > application > overrides > overrides items > oneOf > item 3 > w_layer_neg_opt > options > options items

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

Must be one of:
* "activation_trigger_down"
* "activation_required_mod_down"
* "activation_negative_mod_up"
* "all_activations"
* "one_mod"
* "no_reregister_trigger"
* "no_unregister_on_other_key_down"
* "default"

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2023-05-30 at 22:29:17 +0900
