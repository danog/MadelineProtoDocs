---
title: contacts.blockedSlice
description: Incomplete list of blocked users.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contacts.blockedSlice  
[Back to constructors index](index.md)



Incomplete list of blocked users.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](../types/int.md) | Yes|Total number of elements in the list|
|blocked|Array of [ContactBlocked](../types/ContactBlocked.md) | Yes|Blocked|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [contacts\_Blocked](../types/contacts_Blocked.md)


### Example:

```php
$contacts_blockedSlice = ['_' => 'contacts.blockedSlice', 'count' => int, 'blocked' => [ContactBlocked, ContactBlocked], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
contacts_blockedSlice={_='contacts.blockedSlice', count=int, blocked={ContactBlocked}, users={User}}

```


