---
title: messageActionChannelMigrateFrom
description: Message action channel migrate from
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChannelMigrateFrom  
[Back to constructors index](index.md)



Message action channel migrate from

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](../types/string.md) | Yes|Title|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionChannelMigrateFrom = ['_' => 'messageActionChannelMigrateFrom', 'title' => 'string', 'chat_id' => int];
```  


Or, if you're into Lua:

```lua
messageActionChannelMigrateFrom={_='messageActionChannelMigrateFrom', title='string', chat_id=int}

```


