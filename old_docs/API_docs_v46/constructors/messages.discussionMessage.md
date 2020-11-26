---
title: messages.discussionMessage
description: messages.discussionMessage attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_discussionMessage.html
---
# Constructor: messages.discussionMessage  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|messages|Array of [Message](../types/Message.md) | Yes|
|max\_id|[int](../types/int.md) | Optional|
|read\_inbox\_max\_id|[int](../types/int.md) | Optional|
|read\_outbox\_max\_id|[int](../types/int.md) | Optional|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [messages.DiscussionMessage](../types/messages.DiscussionMessage.md)


### Example:

```php
$messages.discussionMessage = ['_' => 'messages.discussionMessage', 'messages' => [Message, Message], 'max_id' => int, 'read_inbox_max_id' => int, 'read_outbox_max_id' => int, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages.discussionMessage={_='messages.discussionMessage', messages={Message}, max_id=int, read_inbox_max_id=int, read_outbox_max_id=int, chats={Chat}, users={User}}

```


