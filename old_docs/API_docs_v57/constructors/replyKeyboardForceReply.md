---
title: replyKeyboardForceReply
description: replyKeyboardForceReply attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: replyKeyboardForceReply  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|single\_use|[Bool](../types/Bool.md) | Optional|
|selective|[Bool](../types/Bool.md) | Optional|



### Type: [ReplyMarkup](../types/ReplyMarkup.md)


### Example:

```php
$replyKeyboardForceReply = ['_' => 'replyKeyboardForceReply', 'single_use' => Bool, 'selective' => Bool];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "replyKeyboardForceReply", "single_use": Bool, "selective": Bool}
```


Or, if you're into Lua:

```lua
replyKeyboardForceReply={_='replyKeyboardForceReply', single_use=Bool, selective=Bool}

```


