---
title: keyboardButtonRow
description: keyboardButtonRow attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonRow  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|buttons|Array of [KeyboardButton](../types/KeyboardButton.md) | Yes|



### Type: [KeyboardButtonRow](../types/KeyboardButtonRow.md)


### Example:

```php
$keyboardButtonRow = ['_' => 'keyboardButtonRow', 'buttons' => [KeyboardButton, KeyboardButton]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "keyboardButtonRow", "buttons": [KeyboardButton]}
```


Or, if you're into Lua:

```lua
keyboardButtonRow={_='keyboardButtonRow', buttons={KeyboardButton}}

```


