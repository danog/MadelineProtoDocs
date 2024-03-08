---
title: "messages.webPage"
description: "Represents an Instant View webpage."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_webPage.html
---
# Constructor: messages.webPage  
[Back to constructors index](/API_docs/constructors/index.html)



Represents an Instant View webpage.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|webpage|[WebPage](/API_docs/types/WebPage.html) | Optional|The instant view webpage.|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats mentioned in the webpage.|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned in the webpage.|



### Type: [messages.WebPage](/API_docs/types/messages.WebPage.html)


### Example:

```
$messages_webPage = ['_' => 'messages.webPage', 'webpage' => WebPage, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
