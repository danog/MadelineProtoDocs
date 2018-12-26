---
title: replyKeyboardMarkup
description: Reply keyboard markup
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: replyKeyboardMarkup  
[Back to constructors index](index.md)



Reply keyboard markup

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|resize|[Bool](../types/Bool.md) | Optional|Resize?|
|single\_use|[Bool](../types/Bool.md) | Optional|Single use?|
|selective|[Bool](../types/Bool.md) | Optional|Selective?|
|rows|Array of [KeyboardButtonRow](../types/KeyboardButtonRow.md) | Yes|Rows|



### Type: [ReplyMarkup](../types/ReplyMarkup.md)


### Example:

```php
$replyKeyboardMarkup = ['_' => 'replyKeyboardMarkup', 'resize' => Bool, 'single_use' => Bool, 'selective' => Bool, 'rows' => [KeyboardButtonRow, KeyboardButtonRow]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "replyKeyboardMarkup", "resize": Bool, "single_use": Bool, "selective": Bool, "rows": [KeyboardButtonRow]}
```


Or, if you're into Lua:

```lua
replyKeyboardMarkup={_='replyKeyboardMarkup', resize=Bool, single_use=Bool, selective=Bool, rows={KeyboardButtonRow}}

```


