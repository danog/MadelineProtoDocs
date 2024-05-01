---
title: "messages.forumTopics"
description: "Contains information about multiple forum topics"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_forumTopics.html
---
# Constructor: messages.forumTopics  
[Back to constructors index](/API_docs/constructors/index.html)



Contains information about multiple [forum topics](https://core.telegram.org/api/forum#forum-topics)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|order\_by\_create\_date|[Bool](/API_docs/types/Bool.html) | Optional|Whether the returned topics are ordered by creation date; if set, pagination by `offset_date` should use [forumTopic](../constructors/forumTopic.html).`date`; otherwise topics are ordered by the last message date, so paginate by the `date` of the [message](../types/Message.html) referenced by [forumTopic](../constructors/forumTopic.html).`top_message`.|
|count|[int](/API_docs/types/int.html) | Yes|Total number of topics matching query; may be more than the topics contained in `topics`, in which case [pagination](https://core.telegram.org/api/offsets) is required.|
|topics|Array of [ForumTopic](/API_docs/types/ForumTopic.html) | Yes|Forum topics|
|messages|Array of [Message](/API_docs/types/Message.html) | Yes|Related messages (contains the messages mentioned by [forumTopic](../constructors/forumTopic.html).`top_message`).|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Related chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Related users|
|pts|[int](/API_docs/types/int.html) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|



### Type: [messages.ForumTopics](/API_docs/types/messages.ForumTopics.html)


### Example:

```
$messages_forumTopics = ['_' => 'messages.forumTopics', 'order_by_create_date' => Bool, 'count' => int, 'topics' => [ForumTopic, ForumTopic], 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User], 'pts' => int];
```  
