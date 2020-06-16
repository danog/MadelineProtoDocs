---
title: inputPhoneContact
description: Phone contact. The `client_id` is just an arbitrary contact ID: it should be set, for example, to an incremental number when using [contacts.importContacts](../methods/contacts.importContacts.md), in order to retry importing only the contacts that weren't imported successfully.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPhoneContact  
[Back to constructors index](index.md)



Phone contact. The `client_id` is just an arbitrary contact ID: it should be set, for example, to an incremental number when using [contacts.importContacts](../methods/contacts.importContacts.md), in order to retry importing only the contacts that weren't imported successfully.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|client\_id|[long](../types/long.md) | Yes|User identifier on the client|
|phone|[string](../types/string.md) | Yes|Phone number|
|first\_name|[string](../types/string.md) | Yes|Contact's first name|
|last\_name|[string](../types/string.md) | Yes|Contact's last name|



### Type: [InputContact](../types/InputContact.md)


### Example:

```php
$inputPhoneContact = ['_' => 'inputPhoneContact', 'client_id' => long, 'phone' => 'string', 'first_name' => 'string', 'last_name' => 'string'];
```  


Or, if you're into Lua:

```lua
inputPhoneContact={_='inputPhoneContact', client_id=long, phone='string', first_name='string', last_name='string'}

```


