---
title: contacts.blocked
description: Full list of blocked users.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contacts.blocked  
[Back to constructors index](index.md)



Full list of blocked users.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|blocked|Array of [ContactBlocked](../types/ContactBlocked.md) | Yes|Blocked|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [contacts.Blocked](../types/contacts.Blocked.md)


### Example:

```php
$contacts.blocked = ['_' => 'contacts.blocked', 'blocked' => [ContactBlocked, ContactBlocked], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
contacts.blocked={_='contacts.blocked', blocked={ContactBlocked}, users={User}}

```


