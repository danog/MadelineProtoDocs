---
title: "messages.messageViews"
description: "View, forward counter + info about replies"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_messageViews.html
---
# Constructor: messages.messageViews  
[Back to constructors index](/API_docs/constructors/index.md)



View, forward counter + info about replies

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|views|Array of [MessageViews](/API_docs/types/MessageViews.md) | Yes|View, forward counter + info about replies|
|chats|Array of [Chat](/API_docs/types/Chat.md) | Yes|Chats mentioned in constructor|
|users|Array of [User](/API_docs/types/User.md) | Yes|Users mentioned in constructor|



### Type: [messages.MessageViews](/API_docs/types/messages.MessageViews.md)


### Example:

```php
$messages_messageViews = ['_' => 'messages.messageViews', 'views' => [MessageViews, MessageViews], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
