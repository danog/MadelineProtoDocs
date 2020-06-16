---
title: updates.channelDifferenceTooLong
description: The provided `pts + limit < remote pts`. Simply, there are too many updates to be fetched (more than `limit`), the client has to resolve the update gap in one of the following ways:

1. Delete all known messages in the chat, begin from scratch by refetching all messages manually with [getHistory](../methods/messages.getHistory.md). It is easy to implement, but suddenly disappearing messages looks awful for the user.
2. Save all messages loaded in the memory until application restart, but delete all messages from database. Messages left in the memory must be lazily updated using calls to [getHistory](../methods/messages.getHistory.md). It looks much smoothly for the user, he will need to redownload messages only after client restart. Unsynchronized messages left in the memory shouldn't be saved to database, results of [getHistory](../methods/messages.getHistory.md) and [getMessages](../methods/messages.getMessages.md) must be used to update state of deleted and edited messages left in the memory.
3. Save all messages loaded in the memory and stored in the database without saving that some messages form continuous ranges. Messages in the database will be excluded from results of getChatHistory and searchChatMessages after application restart and will be available only through getMessage. Every message should still be checked using getHistory. It has more disadvantages over 2) than advantages.
4. Save all messages with saving all data about continuous message ranges. Messages from the database may be used as results of getChatHistory and (if implemented continuous ranges support for searching shared media) searchChatMessages. The messages should still be lazily checked using getHistory, but they are still available offline. It is the best way for gaps support, but it is pretty hard to implement correctly. It should be also noted that some messages like live location messages shouldn't be deleted.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/updates_channelDifferenceTooLong.html
---
# Constructor: updates.channelDifferenceTooLong  
[Back to constructors index](index.md)



The provided `pts + limit < remote pts`. Simply, there are too many updates to be fetched (more than `limit`), the client has to resolve the update gap in one of the following ways:

1. Delete all known messages in the chat, begin from scratch by refetching all messages manually with [getHistory](../methods/messages.getHistory.md). It is easy to implement, but suddenly disappearing messages looks awful for the user.
2. Save all messages loaded in the memory until application restart, but delete all messages from database. Messages left in the memory must be lazily updated using calls to [getHistory](../methods/messages.getHistory.md). It looks much smoothly for the user, he will need to redownload messages only after client restart. Unsynchronized messages left in the memory shouldn't be saved to database, results of [getHistory](../methods/messages.getHistory.md) and [getMessages](../methods/messages.getMessages.md) must be used to update state of deleted and edited messages left in the memory.
3. Save all messages loaded in the memory and stored in the database without saving that some messages form continuous ranges. Messages in the database will be excluded from results of getChatHistory and searchChatMessages after application restart and will be available only through getMessage. Every message should still be checked using getHistory. It has more disadvantages over 2) than advantages.
4. Save all messages with saving all data about continuous message ranges. Messages from the database may be used as results of getChatHistory and (if implemented continuous ranges support for searching shared media) searchChatMessages. The messages should still be lazily checked using getHistory, but they are still available offline. It is the best way for gaps support, but it is pretty hard to implement correctly. It should be also noted that some messages like live location messages shouldn't be deleted.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|final|[Bool](../types/Bool.md) | Optional|Whether there are more updates that must be fetched (always false)|
|timeout|[int](../types/int.md) | Optional|Clients are supposed to refetch the channel difference after timeout seconds have elapsed|
|dialog|[Dialog](../types/Dialog.md) | Yes|Dialog containing the latest [PTS](https://core.telegram.org/api/updates) that can be used to reset the channel state|
|messages|Array of [Message](../types/Message.md) | Yes|The latest messages|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats from messages|
|users|Array of [User](../types/User.md) | Yes|Users from messages|



### Type: [updates.ChannelDifference](../types/updates.ChannelDifference.md)


### Example:

```php
$updates.channelDifferenceTooLong = ['_' => 'updates.channelDifferenceTooLong', 'final' => Bool, 'timeout' => int, 'dialog' => Dialog, 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
updates.channelDifferenceTooLong={_='updates.channelDifferenceTooLong', final=Bool, timeout=int, dialog=Dialog, messages={Message}, chats={Chat}, users={User}}

```


