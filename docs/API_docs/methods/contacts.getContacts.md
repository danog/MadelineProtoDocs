---
title: "contacts.getContacts"
description: "Returns the current user's contact list."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_getContacts.html
---
# Method: contacts.getContacts
[Back to methods index](index.html)



Returns the current user's contact list.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|[long](/API_docs/types/long.html) | If there already is a full contact list on the client, a [hash](https://core.telegram.org/api/offsets#hash-generation) of a the list of contact IDs in ascending order may be passed in this parameter. If the contact set was not changed, [(contacts.contactsNotModified)](../constructors/contacts.contactsNotModified.html) will be returned. | Yes|


### Return type: [contacts.Contacts](/API_docs/types/contacts.Contacts.html)

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
$contacts_Contacts = $MadelineProto->contacts->getContacts(hash: long, );
```

