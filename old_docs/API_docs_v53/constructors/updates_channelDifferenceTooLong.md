---
title: updates.channelDifferenceTooLong
description: Channel difference too long
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updates.channelDifferenceTooLong  
[Back to constructors index](index.md)



Channel difference too long

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|final|[Bool](../types/Bool.md) | Optional|Final?|
|pts|[int](../types/int.md) | Yes|Pts|
|timeout|[int](../types/int.md) | Optional|Timeout|
|top\_message|[int](../types/int.md) | Yes|Top message|
|read\_inbox\_max\_id|[int](../types/int.md) | Yes|Read inbox max ID|
|read\_outbox\_max\_id|[int](../types/int.md) | Yes|Read outbox max ID|
|unread\_count|[int](../types/int.md) | Yes|Unread count|
|messages|Array of [Message](../types/Message.md) | Yes|Messages|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [updates\_ChannelDifference](../types/updates_ChannelDifference.md)


### Example:

```php
$updates_channelDifferenceTooLong = ['_' => 'updates.channelDifferenceTooLong', 'final' => Bool, 'pts' => int, 'timeout' => int, 'top_message' => int, 'read_inbox_max_id' => int, 'read_outbox_max_id' => int, 'unread_count' => int, 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
updates_channelDifferenceTooLong={_='updates.channelDifferenceTooLong', final=Bool, pts=int, timeout=int, top_message=int, read_inbox_max_id=int, read_outbox_max_id=int, unread_count=int, messages={Message}, chats={Chat}, users={User}}

```


