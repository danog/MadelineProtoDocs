---
title: "messages.webPage"
description: "messages.webPage attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_webPage.html
---
# Constructor: messages.webPage  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|webpage|[WebPage](/API_docs/types/WebPage.html) | Optional|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [messages.WebPage](/API_docs/types/messages.WebPage.html)


### Example:

```
$messages_webPage = ['_' => 'messages.webPage', 'webpage' => WebPage, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
