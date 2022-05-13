---
title: "updates.channelDifferenceTooLong"
description: "The provided pts + limit < remote pts. Simply, there are too many updates to be fetched (more than limit), the client has to resolve the update gap in one of the following ways (assuming the existence of a persistent database to locally store messages)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/updates_channelDifferenceTooLong.html
---
# Constructor: updates.channelDifferenceTooLong  
[Back to constructors index](/API_docs/constructors/index.html)



The provided `pts + limit < remote pts`. Simply, there are too many updates to be fetched (more than `limit`), the client has to resolve the update gap in one of the following ways (assuming the existence of a persistent database to locally store messages):

1. Delete all known messages in the chat, begin from scratch by refetching all messages manually with [messages.getHistory](../methods/messages.getHistory.html). It is easy to implement, but suddenly disappearing messages look awful to the user.
2. Save all messages loaded in the memory until application restart, but delete all messages from the database. Messages left in the memory must be lazily updated using calls to [messages.getHistory](../methods/messages.getHistory.html).  
  It will look much smoother to the user, they will need to redownload messages only after client restart.  
  Unsynchronized messages left in memory shouldn't be saved to the database, results of [messages.getHistory](../methods/messages.getHistory.html) and [messages.getMessages](../methods/messages.getMessages.html) must be used to update the state of deleted and edited messages left in the memory.
3. Save all messages loaded in the memory and stored in the database without saving that some messages form continuous ranges.  
  Messages in the database will be excluded when paginating through or searching the local message history after application restart and will be available only through individual message queries.  
  Every message should still be checked using [messages.getHistory](../methods/messages.getHistory.html).  
  It has more disadvantages over 2) than advantages.
4. Save all messages with saving all data about continuous message ranges.  
  Messages from the database may be used when paginating through or searching the local message history.  
  The messages should still be lazily checked using [messages.getHistory](../methods/messages.getHistory.html), but they are still available offline.  
  It is the best way for gaps support, but it is pretty hard to implement correctly.

It should be also noted that some messages like live location messages shouldn't be deleted.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|final|[Bool](/API_docs/types/Bool.html) | Optional|Whether there are more updates that must be fetched (always false)|
|timeout|[int](/API_docs/types/int.html) | Optional|Clients are supposed to refetch the channel difference after timeout seconds have elapsed|
|dialog|[Dialog](/API_docs/types/Dialog.html) | Yes|Dialog containing the latest [PTS](https://core.telegram.org/api/updates) that can be used to reset the channel state|
|messages|Array of [Message](/API_docs/types/Message.html) | Yes|The latest messages|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats from messages|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users from messages|



### Type: [updates.ChannelDifference](/API_docs/types/updates.ChannelDifference.html)


### Example:

```
$updates_channelDifferenceTooLong = ['_' => 'updates.channelDifferenceTooLong', 'final' => Bool, 'timeout' => int, 'dialog' => Dialog, 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
