---
title: keyboardButtonSwitchInline
description: Keyboard button switch inline
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonSwitchInline  
[Back to constructors index](index.md)



Keyboard button switch inline

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|same\_peer|[Bool](../types/Bool.md) | Optional|Same peer?|
|text|[string](../types/string.md) | Yes|Text|
|query|[string](../types/string.md) | Yes|Query|



### Type: [KeyboardButton](../types/KeyboardButton.md)


### Example:

```php
$keyboardButtonSwitchInline = ['_' => 'keyboardButtonSwitchInline', 'same_peer' => Bool, 'text' => 'string', 'query' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "keyboardButtonSwitchInline", "same_peer": Bool, "text": "string", "query": "string"}
```


Or, if you're into Lua:

```lua
keyboardButtonSwitchInline={_='keyboardButtonSwitchInline', same_peer=Bool, text='string', query='string'}

```


