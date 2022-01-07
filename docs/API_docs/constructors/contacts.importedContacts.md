---
title: "contacts.importedContacts"
description: "Info on succesfully imported contacts."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/contacts_importedContacts.html
---
# Constructor: contacts.importedContacts  
[Back to constructors index](/API_docs/constructors/index.md)



Info on succesfully imported contacts.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|imported|Array of [ImportedContact](/API_docs/types/ImportedContact.md) | Yes|List of succesfully imported contacts|
|popular\_invites|Array of [PopularContact](/API_docs/types/PopularContact.md) | Yes|Popular contacts|
|retry\_contacts|Array of [long](/API_docs/types/long.md) | Yes|List of contact ids that could not be imported due to system limitation and will need to be imported at a later date.<br>Parameter added in [Layer 13](https://core.telegram.org/api/layers#layer-13)|
|users|Array of [User](/API_docs/types/User.md) | Yes|List of users|



### Type: [contacts.ImportedContacts](/API_docs/types/contacts.ImportedContacts.md)


### Example:

```php
$contacts_importedContacts = ['_' => 'contacts.importedContacts', 'imported' => [ImportedContact, ImportedContact], 'popular_invites' => [PopularContact, PopularContact], 'retry_contacts' => [long, long], 'users' => [User, User]];
```  
