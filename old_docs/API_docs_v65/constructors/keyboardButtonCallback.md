---
title: keyboardButtonCallback
description: Keyboard button callback
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonCallback  
[Back to constructors index](index.md)



Keyboard button callback

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](../types/string.md) | Yes|Text|
|data|[bytes](../types/bytes.md) | Yes|Data|



### Type: [KeyboardButton](../types/KeyboardButton.md)


### Example:

```php
$keyboardButtonCallback = ['_' => 'keyboardButtonCallback', 'text' => 'string', 'data' => 'bytes'];
```  


Or, if you're into Lua:

```lua
keyboardButtonCallback={_='keyboardButtonCallback', text='string', data='bytes'}

```


