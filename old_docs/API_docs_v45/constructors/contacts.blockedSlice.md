---
title: contacts.blockedSlice
description: Incomplete list of blocked users.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/contacts_blockedSlice.html
---
# Constructor: contacts.blockedSlice  
[Back to constructors index](index.md)



Incomplete list of blocked users.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](../types/int.md) | Yes|Total number of elements in the list|
|blocked|Array of [PeerBlocked](../types/PeerBlocked.md) | Yes|List of blocked users|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|List of users|



### Type: [contacts.Blocked](../types/contacts.Blocked.md)


### Example:

```php
$contacts.blockedSlice = ['_' => 'contacts.blockedSlice', 'count' => int, 'blocked' => [PeerBlocked, PeerBlocked], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
contacts.blockedSlice={_='contacts.blockedSlice', count=int, blocked={PeerBlocked}, chats={Chat}, users={User}}

```


