---
title: "contacts.importedContacts"
description: "Info on successfully imported contacts."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/contacts_importedContacts.html
---
# Constructor: contacts.importedContacts  
[Back to constructors index](/API_docs/constructors/index.html)



Info on successfully imported contacts.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|imported|Array of [ImportedContact](/API_docs/types/ImportedContact.html) | Yes|List of successfully imported contacts|
|popular\_invites|Array of [PopularContact](/API_docs/types/PopularContact.html) | Yes|Popular contacts|
|retry\_contacts|Array of [long](/API_docs/types/long.html) | Yes|List of contact ids that could not be imported due to system limitation and will need to be imported at a later date.<br>Parameter added in [Layer 13](https://core.telegram.org/api/layers#layer-13)|
|users|Array of [User](/API_docs/types/User.html) | Yes|List of users|



### Type: [contacts.ImportedContacts](/API_docs/types/contacts.ImportedContacts.html)


### Example:

```
$contacts_importedContacts = ['_' => 'contacts.importedContacts', 'imported' => [ImportedContact, ImportedContact], 'popular_invites' => [PopularContact, PopularContact], 'retry_contacts' => [long, long], 'users' => [User, User]];
```  
