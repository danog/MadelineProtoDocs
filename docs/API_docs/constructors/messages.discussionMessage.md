---
title: "messages.discussionMessage"
description: "Information about a message thread"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_discussionMessage.html
---
# Constructor: messages.discussionMessage  
[Back to constructors index](/API_docs/constructors/index.html)



Information about a [message thread](https://core.telegram.org/api/threads)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|messages|Array of [Message](/API_docs/types/Message.html) | Yes|Discussion messages|
|max\_id|[int](/API_docs/types/int.html) | Optional|Message ID of latest reply in this [thread](https://core.telegram.org/api/threads)|
|read\_inbox\_max\_id|[int](/API_docs/types/int.html) | Optional|Message ID of latest read incoming message in this [thread](https://core.telegram.org/api/threads)|
|read\_outbox\_max\_id|[int](/API_docs/types/int.html) | Optional|Message ID of latest read outgoing message in this [thread](https://core.telegram.org/api/threads)|
|unread\_count|[int](/API_docs/types/int.html) | Yes|Number of unread messages|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats mentioned in constructor|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned in constructor|



### Type: [messages.DiscussionMessage](/API_docs/types/messages.DiscussionMessage.html)


### Example:

```
$messages_discussionMessage = ['_' => 'messages.discussionMessage', 'messages' => [Message, Message], 'max_id' => int, 'read_inbox_max_id' => int, 'read_outbox_max_id' => int, 'unread_count' => int, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
