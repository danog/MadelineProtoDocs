---
title: contacts.topPeers
description: Top peers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contacts.topPeers  
[Back to constructors index](index.md)



Top peers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|categories|Array of [TopPeerCategoryPeers](../types/TopPeerCategoryPeers.md) | Yes|Categories|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [contacts\_TopPeers](../types/contacts_TopPeers.md)


### Example:

```php
$contacts_topPeers = ['_' => 'contacts.topPeers', 'categories' => [TopPeerCategoryPeers, TopPeerCategoryPeers], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "contacts.topPeers", "categories": [TopPeerCategoryPeers], "chats": [Chat], "users": [User]}
```


Or, if you're into Lua:

```lua
contacts_topPeers={_='contacts.topPeers', categories={TopPeerCategoryPeers}, chats={Chat}, users={User}}

```


