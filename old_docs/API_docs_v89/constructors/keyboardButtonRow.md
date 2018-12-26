---
title: keyboardButtonRow
description: Keyboard button row
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonRow  
[Back to constructors index](index.md)



Keyboard button row

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|buttons|Array of [KeyboardButton](../types/KeyboardButton.md) | Yes|Buttons|



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


