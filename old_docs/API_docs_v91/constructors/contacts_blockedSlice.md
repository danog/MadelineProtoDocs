---
title: contacts.blockedSlice
description: Blocked slice
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contacts.blockedSlice  
[Back to constructors index](index.md)



Blocked slice

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](../types/int.md) | Yes|Count|
|blocked|Array of [ContactBlocked](../types/ContactBlocked.md) | Yes|Blocked|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [contacts\_Blocked](../types/contacts_Blocked.md)


### Example:

```php
$contacts_blockedSlice = ['_' => 'contacts.blockedSlice', 'count' => int, 'blocked' => [ContactBlocked, ContactBlocked], 'users' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "contacts.blockedSlice", "count": int, "blocked": [ContactBlocked], "users": [User]}
```


Or, if you're into Lua:

```lua
contacts_blockedSlice={_='contacts.blockedSlice', count=int, blocked={ContactBlocked}, users={User}}

```


