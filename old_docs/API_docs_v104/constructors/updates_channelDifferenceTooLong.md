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
|timeout|[int](../types/int.md) | Optional|Timeout|
|dialog|[Dialog](../types/Dialog.md) | Yes|Dialog|
|messages|Array of [Message](../types/Message.md) | Yes|Messages|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [updates\_ChannelDifference](../types/updates_ChannelDifference.md)


### Example:

```php
$updates_channelDifferenceTooLong = ['_' => 'updates.channelDifferenceTooLong', 'final' => Bool, 'timeout' => int, 'dialog' => Dialog, 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
updates_channelDifferenceTooLong={_='updates.channelDifferenceTooLong', final=Bool, timeout=int, dialog=Dialog, messages={Message}, chats={Chat}, users={User}}

```


