---
title: "contacts.importContacts"
description: "Imports contacts: saves a full list on the server, adds already registered contacts to the contact list, returns added contacts and their info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_importContacts.html
---
# Method: contacts.importContacts
[Back to methods index](index.html)



Imports contacts: saves a full list on the server, adds already registered contacts to the contact list, returns added contacts and their info.

Use [contacts.addContact](../methods/contacts.addContact.html) to add Telegram contacts without actually using their phone number.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|contacts|Array of [InputContact](/API_docs/types/InputContact.html) | List of contacts to import | Yes|


### Return type: [contacts.ImportedContacts](/API_docs/types/contacts.ImportedContacts.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$contacts_ImportedContacts = $MadelineProto->contacts->importContacts(contacts: [InputContact, InputContact], );
```

