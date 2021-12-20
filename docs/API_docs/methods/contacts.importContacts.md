---
title: "contacts.importContacts"
description: "Imports contacts: saves a full list on the server, adds already registered contacts to the contact list, returns added contacts and their info."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_importContacts.html
---
# Method: contacts.importContacts
[Back to methods index](index.md)



Imports contacts: saves a full list on the server, adds already registered contacts to the contact list, returns added contacts and their info.

Use [contacts.addContact](../methods/contacts.addContact.md) to add Telegram contacts without actually using their phone number.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|contacts|Array of [InputContact](../types/InputContact.md) | List of contacts to import | Yes|


### Return type: [contacts.ImportedContacts](../types/contacts.ImportedContacts.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$contacts_ImportedContacts = $MadelineProto->contacts->importContacts(['contacts' => [InputContact, InputContact], ]);
```

Or, if you're into Lua:

```lua
contacts_ImportedContacts = contacts.importContacts({contacts={InputContact}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|


