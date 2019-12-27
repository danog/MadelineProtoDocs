---
title: contacts.importedContacts
description: Info on succesfully imported contacts.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contacts.importedContacts  
[Back to constructors index](index.md)



Info on succesfully imported contacts.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|imported|Array of [ImportedContact](../types/ImportedContact.md) | Yes|Imported|
|popular\_invites|Array of [PopularContact](../types/PopularContact.md) | Yes|Popular invites|
|retry\_contacts|Array of [long](../types/long.md) | Yes|Retry importing contacts whose client IDs appear here|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [contacts.ImportedContacts](../types/contacts.ImportedContacts.md)


### Example:

```php
$contacts.importedContacts = ['_' => 'contacts.importedContacts', 'imported' => [ImportedContact, ImportedContact], 'popular_invites' => [PopularContact, PopularContact], 'retry_contacts' => [long, long], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
contacts.importedContacts={_='contacts.importedContacts', imported={ImportedContact}, popular_invites={PopularContact}, retry_contacts={long}, users={User}}

```


