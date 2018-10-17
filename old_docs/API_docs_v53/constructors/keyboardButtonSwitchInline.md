---
title: keyboardButtonSwitchInline
description: keyboardButtonSwitchInline attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonSwitchInline  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|text|[string](../types/string.md) | Yes|
|query|[string](../types/string.md) | Yes|



### Type: [KeyboardButton](../types/KeyboardButton.md)


### Example:

```php
$keyboardButtonSwitchInline = ['_' => 'keyboardButtonSwitchInline', 'text' => 'string', 'query' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "keyboardButtonSwitchInline", "text": "string", "query": "string"}
```


Or, if you're into Lua:

```lua
keyboardButtonSwitchInline={_='keyboardButtonSwitchInline', text='string', query='string'}

```


