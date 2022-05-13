---
title: "messages.sponsoredMessages"
description: "A set of sponsored messages associated to a channel"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_sponsoredMessages.html
---
# Constructor: messages.sponsoredMessages  
[Back to constructors index](/API_docs/constructors/index.html)



A set of sponsored messages associated to a channel

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|messages|Array of [SponsoredMessage](/API_docs/types/SponsoredMessage.html) | Yes|Sponsored messages|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats mentioned in the sponsored messages|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned in the sponsored messages|



### Type: [messages.SponsoredMessages](/API_docs/types/messages.SponsoredMessages.html)


### Example:

```
$messages_sponsoredMessages = ['_' => 'messages.sponsoredMessages', 'messages' => [SponsoredMessage, SponsoredMessage], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
