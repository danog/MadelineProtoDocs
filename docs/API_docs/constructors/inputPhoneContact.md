---
title: "inputPhoneContact"
description: "Phone contact. The client_id is just an arbitrary contact ID: it should be set, for example, to an incremental number when using contacts.importContacts, in order to retry importing only the contacts that weren't imported successfully."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPhoneContact  
[Back to constructors index](/API_docs/constructors/index.md)



Phone contact. The `client_id` is just an arbitrary contact ID: it should be set, for example, to an incremental number when using [contacts.importContacts](../methods/contacts.importContacts.md), in order to retry importing only the contacts that weren't imported successfully.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|client\_id|[long](/API_docs/types/long.md) | Yes|User identifier on the client|
|phone|[string](/API_docs/types/string.md) | Yes|Phone number|
|first\_name|[string](/API_docs/types/string.md) | Yes|Contact's first name|
|last\_name|[string](/API_docs/types/string.md) | Yes|Contact's last name|



### Type: [InputContact](/API_docs/types/InputContact.md)


### Example:

```php
$inputPhoneContact = ['_' => 'inputPhoneContact', 'client_id' => long, 'phone' => 'string', 'first_name' => 'string', 'last_name' => 'string'];
```  
