---
title: "contacts.resolvedPeer"
description: "Resolved peer"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/contacts_resolvedPeer.html
---
# Constructor: contacts.resolvedPeer  
[Back to constructors index](/API_docs/constructors/index.html)



Resolved peer

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|The peer|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users|



### Type: [contacts.ResolvedPeer](/API_docs/types/contacts.ResolvedPeer.html)


### Example:

```
$contacts_resolvedPeer = ['_' => 'contacts.resolvedPeer', 'peer' => Peer, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
