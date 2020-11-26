---
title: contacts.getContacts
description: Returns the current user's contact list.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_getContacts.html
---
# Method: contacts.getContacts
[Back to methods index](index.md)



Returns the current user's contact list.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [int](../types/int.md) | If there already is a full contact list on the client, a [hash](https://core.telegram.org/api/offsets#hash-generation) of a the list of contact IDs in ascending order may be passed in this parameter. If the contact set was not changed, [(contacts.contactsNotModified)](../constructors/contacts.contactsNotModified.md) will be returned. | Optional|


### Return type: [contacts.Contacts](../types/contacts.Contacts.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$contacts.Contacts = $MadelineProto->contacts->getContacts(['hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
contacts.Contacts = contacts.getContacts({hash={int}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|


