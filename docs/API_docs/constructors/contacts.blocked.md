---
title: "contacts.blocked"
description: "Full list of blocked users."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/contacts_blocked.html
---
# Constructor: contacts.blocked  
[Back to constructors index](index.md)



Full list of blocked users.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|blocked|Array of [PeerBlocked](../types/PeerBlocked.md) | Yes|List of blocked users|
|chats|Array of [Chat](../types/Chat.md) | Yes|Blocked chats|
|users|Array of [User](../types/User.md) | Yes|List of users|



### Type: [contacts.Blocked](../types/contacts.Blocked.md)


### Example:

```php
$contacts_blocked = ['_' => 'contacts.blocked', 'blocked' => [PeerBlocked, PeerBlocked], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
contacts_blocked={_='contacts.blocked', blocked={PeerBlocked}, chats={Chat}, users={User}}

```


