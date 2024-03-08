---
title: "messages.quickReplies"
description: "messages.quickReplies attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_quickReplies.html
---
# Constructor: messages.quickReplies  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|quick\_replies|Array of [QuickReply](/API_docs/types/QuickReply.html) | Yes|
|messages|Array of [Message](/API_docs/types/Message.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [messages.QuickReplies](/API_docs/types/messages.QuickReplies.html)


### Example:

```
$messages_quickReplies = ['_' => 'messages.quickReplies', 'quick_replies' => [QuickReply, QuickReply], 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
