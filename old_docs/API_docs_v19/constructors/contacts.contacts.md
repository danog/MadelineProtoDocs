---
title: contacts.contacts
description: The current user's contact list and info on users.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/contacts_contacts.html
---
# Constructor: contacts.contacts  
[Back to constructors index](index.md)



The current user's contact list and info on users.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|contacts|Array of [Contact](../types/Contact.md) | Yes|Contact list|
|users|Array of [User](../types/User.md) | Yes|User list|



### Type: [contacts.Contacts](../types/contacts.Contacts.md)


### Example:

```php
$contacts_contacts = ['_' => 'contacts.contacts', 'contacts' => [Contact, Contact], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
contacts_contacts={_='contacts.contacts', contacts={Contact}, users={User}}

```


