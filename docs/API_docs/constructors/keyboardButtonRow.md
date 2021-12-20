---
title: "keyboardButtonRow"
description: "Inline keyboard row"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonRow  
[Back to constructors index](index.md)



Inline keyboard row

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|buttons|Array of [KeyboardButton](../types/KeyboardButton.md) | Yes|Bot or inline keyboard buttons|



### Type: [KeyboardButtonRow](../types/KeyboardButtonRow.md)


### Example:

```php
$keyboardButtonRow = ['_' => 'keyboardButtonRow', 'buttons' => [KeyboardButton, KeyboardButton]];
```  


Or, if you're into Lua:

```lua
keyboardButtonRow={_='keyboardButtonRow', buttons={KeyboardButton}}

```


