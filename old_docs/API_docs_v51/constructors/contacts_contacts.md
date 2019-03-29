---
title: contacts.contacts
description: Contacts
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contacts.contacts  
[Back to constructors index](index.md)



Contacts

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|contacts|Array of [Contact](../types/Contact.md) | Yes|Contacts|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [contacts\_Contacts](../types/contacts_Contacts.md)


### Example:

```php
$contacts_contacts = ['_' => 'contacts.contacts', 'contacts' => [Contact, Contact], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
contacts_contacts={_='contacts.contacts', contacts={Contact}, users={User}}

```


