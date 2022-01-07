---
title: "messages.sponsoredMessages"
description: "messages.sponsoredMessages attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_sponsoredMessages.html
---
# Constructor: messages.sponsoredMessages  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|messages|Array of [SponsoredMessage](../types/SponsoredMessage.md) | Yes|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [messages.SponsoredMessages](../types/messages.SponsoredMessages.md)


### Example:

```php
$messages_sponsoredMessages = ['_' => 'messages.sponsoredMessages', 'messages' => [SponsoredMessage, SponsoredMessage], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
