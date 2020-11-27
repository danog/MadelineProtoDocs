---
title: contacts.found
description: Users found by name substring and auxiliary data.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/contacts_found.html
---
# Constructor: contacts.found  
[Back to constructors index](index.md)



Users found by name substring and auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|results|Array of [Peer](../types/Peer.md) | Yes|List of found user identifiers|
|chats|Array of [Chat](../types/Chat.md) | Yes|Found chats|
|users|Array of [User](../types/User.md) | Yes|List of users|



### Type: [contacts.Found](../types/contacts.Found.md)


### Example:

```php
$contacts_found = ['_' => 'contacts.found', 'results' => [Peer, Peer], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
contacts_found={_='contacts.found', results={Peer}, chats={Chat}, users={User}}

```


