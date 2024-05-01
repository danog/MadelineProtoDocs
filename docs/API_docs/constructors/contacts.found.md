---
title: "contacts.found"
description: "Users found by name substring and auxiliary data."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/contacts_found.html
---
# Constructor: contacts.found  
[Back to constructors index](/API_docs/constructors/index.html)



Users found by name substring and auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|my\_results|Array of [Peer](/API_docs/types/Peer.html) | Yes|Personalized results|
|results|Array of [Peer](/API_docs/types/Peer.html) | Yes|List of found user identifiers|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Found chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|List of users|



### Type: [contacts.Found](/API_docs/types/contacts.Found.html)


### Example:

```
$contacts_found = ['_' => 'contacts.found', 'my_results' => [Peer, Peer], 'results' => [Peer, Peer], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
