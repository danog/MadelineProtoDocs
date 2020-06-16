---
title: messageActionChannelMigrateFrom
description: Indicates the channel was [migrated](https://core.telegram.org/api/channel) from the specified chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChannelMigrateFrom  
[Back to constructors index](index.md)



Indicates the channel was [migrated](https://core.telegram.org/api/channel) from the specified chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](../types/string.md) | Yes|The old chat tite|
|chat\_id|[int](../types/int.md) | Yes|The old chat ID|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionChannelMigrateFrom = ['_' => 'messageActionChannelMigrateFrom', 'title' => 'string', 'chat_id' => int];
```  


Or, if you're into Lua:

```lua
messageActionChannelMigrateFrom={_='messageActionChannelMigrateFrom', title='string', chat_id=int}

```


