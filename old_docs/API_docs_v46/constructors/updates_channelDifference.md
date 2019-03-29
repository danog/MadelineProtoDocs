---
title: updates.channelDifference
description: Channel difference
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updates.channelDifference  
[Back to constructors index](index.md)



Channel difference

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|final|[Bool](../types/Bool.md) | Optional|Final?|
|channel\_pts|[int](../types/int.md) | Yes|Channel pts|
|timeout|[int](../types/int.md) | Optional|Timeout|
|new\_messages|Array of [Message](../types/Message.md) | Yes|New messages|
|other\_updates|Array of [Update](../types/Update.md) | Yes|Other updates|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [updates\_ChannelDifference](../types/updates_ChannelDifference.md)


### Example:

```php
$updates_channelDifference = ['_' => 'updates.channelDifference', 'final' => Bool, 'channel_pts' => int, 'timeout' => int, 'new_messages' => [Message, Message], 'other_updates' => [Update, Update], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
updates_channelDifference={_='updates.channelDifference', final=Bool, channel_pts=int, timeout=int, new_messages={Message}, other_updates={Update}, chats={Chat}, users={User}}

```


