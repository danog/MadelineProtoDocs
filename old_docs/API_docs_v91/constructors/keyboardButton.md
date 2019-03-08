---
title: keyboardButton
description: Keyboard button
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButton  
[Back to constructors index](index.md)



Keyboard button

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](../types/string.md) | Yes|Text|



### Type: [KeyboardButton](../types/KeyboardButton.md)


### Example:

```php
$keyboardButton = ['_' => 'keyboardButton', 'text' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "keyboardButton", "text": "string"}
```


Or, if you're into Lua:

```lua
keyboardButton={_='keyboardButton', text='string'}

```


