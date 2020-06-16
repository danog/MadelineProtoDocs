---
title: updates.channelDifference
description: The new updates
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/updates_channelDifference.html
---
# Constructor: updates.channelDifference  
[Back to constructors index](index.md)



The new updates

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pts|[int](../types/int.md) | Yes|The [PTS](https://core.telegram.org/api/updates) from which to start getting updates the next time|
|timeout|[int](../types/int.md) | Optional|Clients are supposed to refetch the channel difference after timeout seconds have elapsed|
|new\_messages|Array of [Message](../types/Message.md) | Yes|New messages|
|other\_updates|Array of [Update](../types/Update.md) | Yes|Other updates|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [updates.ChannelDifference](../types/updates.ChannelDifference.md)


### Example:

```php
$updates.channelDifference = ['_' => 'updates.channelDifference', 'pts' => int, 'timeout' => int, 'new_messages' => [Message, Message], 'other_updates' => [Update, Update], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
updates.channelDifference={_='updates.channelDifference', pts=int, timeout=int, new_messages={Message}, other_updates={Update}, chats={Chat}, users={User}}

```


