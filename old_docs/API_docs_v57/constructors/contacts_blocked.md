---
title: contacts.blocked
description: Blocked
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contacts.blocked  
[Back to constructors index](index.md)



Blocked

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|blocked|Array of [ContactBlocked](../types/ContactBlocked.md) | Yes|Blocked|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [contacts\_Blocked](../types/contacts_Blocked.md)


### Example:

```php
$contacts_blocked = ['_' => 'contacts.blocked', 'blocked' => [ContactBlocked, ContactBlocked], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
contacts_blocked={_='contacts.blocked', blocked={ContactBlocked}, users={User}}

```


