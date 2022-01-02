---
title: "contacts.importedContacts"
description: "Info on succesfully imported contacts."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/contacts_importedContacts.html
---
# Constructor: contacts.importedContacts  
[Back to constructors index](index.md)



Info on succesfully imported contacts.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|imported|Array of [ImportedContact](../types/ImportedContact.md) | Yes|List of succesfully imported contacts|
|popular\_invites|Array of [PopularContact](../types/PopularContact.md) | Yes|Popular contacts|
|retry\_contacts|Array of [long](../types/long.md) | Yes|List of contact ids that could not be imported due to system limitation and will need to be imported at a later date.<br>Parameter added in [Layer 13](https://core.telegram.org/api/layers#layer-13)|
|users|Array of [User](../types/User.md) | Yes|List of users|



### Type: [contacts.ImportedContacts](../types/contacts.ImportedContacts.md)


### Example:

```php
$contacts_importedContacts = ['_' => 'contacts.importedContacts', 'imported' => [ImportedContact, ImportedContact], 'popular_invites' => [PopularContact, PopularContact], 'retry_contacts' => [long, long], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
contacts_importedContacts={_='contacts.importedContacts', imported={ImportedContact}, popular_invites={PopularContact}, retry_contacts={long}, users={User}}

```


