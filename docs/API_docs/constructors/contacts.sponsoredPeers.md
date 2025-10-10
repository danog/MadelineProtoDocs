---
title: "contacts.sponsoredPeers"
description: "Sponsored peers."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/contacts_sponsoredPeers.html
---
# Constructor: contacts.sponsoredPeers  
[Back to constructors index](/API_docs/constructors/index.html)



Sponsored peers.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peers|Array of [SponsoredPeer](/API_docs/types/SponsoredPeer.html) | Yes|Sponsored peers.|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Info about sponsored chats and channels|
|users|Array of [User](/API_docs/types/User.html) | Yes|Info about sponsored users|



### Type: [contacts.SponsoredPeers](/API_docs/types/contacts.SponsoredPeers.html)


### Example:

```
$contacts_sponsoredPeers = ['_' => 'contacts.sponsoredPeers', 'peers' => [SponsoredPeer, SponsoredPeer], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
