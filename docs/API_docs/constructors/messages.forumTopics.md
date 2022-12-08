---
title: "messages.forumTopics"
description: "messages.forumTopics attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_forumTopics.html
---
# Constructor: messages.forumTopics  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|order\_by\_create\_date|[Bool](/API_docs/types/Bool.html) | Optional|
|count|[int](/API_docs/types/int.html) | Yes|
|topics|Array of [ForumTopic](/API_docs/types/ForumTopic.html) | Yes|
|messages|Array of [Message](/API_docs/types/Message.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|
|pts|[int](/API_docs/types/int.html) | Yes|



### Type: [messages.ForumTopics](/API_docs/types/messages.ForumTopics.html)


### Example:

```
$messages_forumTopics = ['_' => 'messages.forumTopics', 'order_by_create_date' => Bool, 'count' => int, 'topics' => [ForumTopic, ForumTopic], 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User], 'pts' => int];
```  
