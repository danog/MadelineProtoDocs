---
title: keyboardButtonUrl
description: Keyboard button URL
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonUrl  
[Back to constructors index](index.md)



Keyboard button URL

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](../types/string.md) | Yes|Text|
|url|[string](../types/string.md) | Yes|URL|



### Type: [KeyboardButton](../types/KeyboardButton.md)


### Example:

```php
$keyboardButtonUrl = ['_' => 'keyboardButtonUrl', 'text' => 'string', 'url' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "keyboardButtonUrl", "text": "string", "url": "string"}
```


Or, if you're into Lua:

```lua
keyboardButtonUrl={_='keyboardButtonUrl', text='string', url='string'}

```


