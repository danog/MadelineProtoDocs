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
|channel\_pts|[int](../types/int.md) | Yes|Channel pts|
|timeout|[int](../types/int.md) | Optional|Timeout|
|top\_message|[int](../types/int.md) | Yes|Top message|
|top\_important\_message|[int](../types/int.md) | Yes|Top important message|
|read\_inbox\_max\_id|[int](../types/int.md) | Yes|Read inbox max ID|
|unread\_count|[int](../types/int.md) | Yes|Unread count|
|unread\_important\_count|[int](../types/int.md) | Yes|Unread important count|
|messages|Array of [Message](../types/Message.md) | Yes|Messages|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [updates\_ChannelDifference](../types/updates_ChannelDifference.md)


### Example:

```php
$updates_channelDifferenceTooLong = ['_' => 'updates.channelDifferenceTooLong', 'final' => Bool, 'channel_pts' => int, 'timeout' => int, 'top_message' => int, 'top_important_message' => int, 'read_inbox_max_id' => int, 'unread_count' => int, 'unread_important_count' => int, 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updates.channelDifferenceTooLong", "final": Bool, "channel_pts": int, "timeout": int, "top_message": int, "top_important_message": int, "read_inbox_max_id": int, "unread_count": int, "unread_important_count": int, "messages": [Message], "chats": [Chat], "users": [User]}
```


Or, if you're into Lua:

```lua
updates_channelDifferenceTooLong={_='updates.channelDifferenceTooLong', final=Bool, channel_pts=int, timeout=int, top_message=int, top_important_message=int, read_inbox_max_id=int, unread_count=int, unread_important_count=int, messages={Message}, chats={Chat}, users={User}}

```


