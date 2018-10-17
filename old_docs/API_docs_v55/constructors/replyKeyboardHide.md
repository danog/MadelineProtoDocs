---
title: replyKeyboardHide
description: replyKeyboardHide attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: replyKeyboardHide  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|selective|[Bool](../types/Bool.md) | Optional|



### Type: [ReplyMarkup](../types/ReplyMarkup.md)


### Example:

```php
$replyKeyboardHide = ['_' => 'replyKeyboardHide', 'selective' => Bool];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "replyKeyboardHide", "selective": Bool}
```


Or, if you're into Lua:

```lua
replyKeyboardHide={_='replyKeyboardHide', selective=Bool}

```


