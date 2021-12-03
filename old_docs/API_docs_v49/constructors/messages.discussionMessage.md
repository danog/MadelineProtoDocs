---
title: messages.discussionMessage
description: Information about a [message thread](https://core.telegram.org/api/threads)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_discussionMessage.html
---
# Constructor: messages.discussionMessage  
[Back to constructors index](index.md)



Information about a [message thread](https://core.telegram.org/api/threads)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|messages|Array of [Message](../types/Message.md) | Yes|Discussion messages|
|max\_id|[int](../types/int.md) | Optional|Message ID of latest reply in this [thread](https://core.telegram.org/api/threads)|
|read\_inbox\_max\_id|[int](../types/int.md) | Optional|Message ID of latest read incoming message in this [thread](https://core.telegram.org/api/threads)|
|read\_outbox\_max\_id|[int](../types/int.md) | Optional|Message ID of latest read outgoing message in this [thread](https://core.telegram.org/api/threads)|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats mentioned in constructor|
|users|Array of [User](../types/User.md) | Yes|Users mentioned in constructor|



### Type: [messages.DiscussionMessage](../types/messages.DiscussionMessage.md)


### Example:

```php
$messages_discussionMessage = ['_' => 'messages.discussionMessage', 'messages' => [Message, Message], 'max_id' => int, 'read_inbox_max_id' => int, 'read_outbox_max_id' => int, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages_discussionMessage={_='messages.discussionMessage', messages={Message}, max_id=int, read_inbox_max_id=int, read_outbox_max_id=int, chats={Chat}, users={User}}

```


