---
title: "messages.webPagePreview"
description: "messages.webPagePreview attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_webPagePreview.html
---
# Constructor: messages.webPagePreview  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|media|[MessageMedia](/API_docs/types/MessageMedia.html) | Optional|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [messages.WebPagePreview](/API_docs/types/messages.WebPagePreview.html)


### Example:

```
$messages_webPagePreview = ['_' => 'messages.webPagePreview', 'media' => MessageMedia, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
