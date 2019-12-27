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
|my\_results|Array of [Peer](../types/Peer.md) | Yes|My results|
|results|Array of [Peer](../types/Peer.md) | Yes|Results|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [contacts.Found](../types/contacts.Found.md)


### Example:

```php
$contacts.found = ['_' => 'contacts.found', 'my_results' => [Peer, Peer], 'results' => [Peer, Peer], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
contacts.found={_='contacts.found', my_results={Peer}, results={Peer}, chats={Chat}, users={User}}

```


