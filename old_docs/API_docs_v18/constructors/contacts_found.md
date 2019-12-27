---
title: contacts.found
description: Users found by name substring and auxiliary data.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contacts.found  
[Back to constructors index](index.md)



Users found by name substring and auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|results|Array of [ContactFound](../types/ContactFound.md) | Yes|Results|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [contacts\_Found](../types/contacts_Found.md)


### Example:

```php
$contacts_found = ['_' => 'contacts.found', 'results' => [ContactFound, ContactFound], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
contacts_found={_='contacts.found', results={ContactFound}, users={User}}

```


