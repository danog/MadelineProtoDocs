---
title: replyKeyboardMarkup
description: Bot keyboard
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: replyKeyboardMarkup  
[Back to constructors index](index.md)



Bot keyboard

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|rows|Array of [KeyboardButtonRow](../types/KeyboardButtonRow.md) | Yes|Button row|



### Type: [ReplyMarkup](../types/ReplyMarkup.md)


### Example:

```php
$replyKeyboardMarkup = ['_' => 'replyKeyboardMarkup', 'rows' => [KeyboardButtonRow, KeyboardButtonRow]];
```  


Or, if you're into Lua:

```lua
replyKeyboardMarkup={_='replyKeyboardMarkup', rows={KeyboardButtonRow}}

```


