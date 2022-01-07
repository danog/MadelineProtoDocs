---
title: "messages.chatAdminsWithInvites"
description: "messages.chatAdminsWithInvites attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_chatAdminsWithInvites.html
---
# Constructor: messages.chatAdminsWithInvites  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|admins|Array of [ChatAdminWithInvites](/API_docs/types/ChatAdminWithInvites.md) | Yes|
|users|Array of [User](/API_docs/types/User.md) | Yes|



### Type: [messages.ChatAdminsWithInvites](/API_docs/types/messages.ChatAdminsWithInvites.md)


### Example:

```php
$messages_chatAdminsWithInvites = ['_' => 'messages.chatAdminsWithInvites', 'admins' => [ChatAdminWithInvites, ChatAdminWithInvites], 'users' => [User, User]];
```  
