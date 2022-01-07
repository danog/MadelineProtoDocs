---
title: "contacts.contacts"
description: "The current user's contact list and info on users."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/contacts_contacts.html
---
# Constructor: contacts.contacts  
[Back to constructors index](/API_docs/constructors/index.md)



The current user's contact list and info on users.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|contacts|Array of [Contact](/API_docs/types/Contact.md) | Yes|Contact list|
|saved\_count|[int](/API_docs/types/int.md) | Yes|Number of contacts that were saved successfully|
|users|Array of [User](/API_docs/types/User.md) | Yes|User list|



### Type: [contacts.Contacts](/API_docs/types/contacts.Contacts.md)


### Example:

```php
$contacts_contacts = ['_' => 'contacts.contacts', 'contacts' => [Contact, Contact], 'saved_count' => int, 'users' => [User, User]];
```  
