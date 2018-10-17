---
title: messageActionChatMigrateTo
description: messageActionChatMigrateTo attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChatMigrateTo  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel\_id|[int](../types/int.md) | Yes|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionChatMigrateTo = ['_' => 'messageActionChatMigrateTo', 'channel_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageActionChatMigrateTo", "channel_id": int}
```


Or, if you're into Lua:

```lua
messageActionChatMigrateTo={_='messageActionChatMigrateTo', channel_id=int}

```


