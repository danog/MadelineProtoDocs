---
title: "contacts.blocked"
description: "Full list of blocked users."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/contacts_blocked.html
---
# Constructor: contacts.blocked  
[Back to constructors index](/API_docs/constructors/index.html)



Full list of blocked users.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|blocked|Array of [PeerBlocked](/API_docs/types/PeerBlocked.html) | Yes|List of blocked users|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Blocked chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|List of users|



### Type: [contacts.Blocked](/API_docs/types/contacts.Blocked.html)


### Example:

```
$contacts_blocked = ['_' => 'contacts.blocked', 'blocked' => [PeerBlocked, PeerBlocked], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
