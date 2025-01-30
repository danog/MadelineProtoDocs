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
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | [Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation).<br>Note that the hash is computed [using the usual algorithm](https://core.telegram.org/api/offsets#hash-generation), passing to the algorithm first the previously returned [contacts.contacts](../constructors/contacts.contacts.html).`saved_count` field, then max `100000` sorted user IDs from the contact list, including the ID of the currently logged in user if it is saved as a contact. <br>Example: [tdlib implementation](https://github.com/tdlib/td/blob/63c7d0301825b78c30dc7307f1f1466be049eb79/td/telegram/UserManager.cpp#L5754). | Optional|


### Return type: [contacts.Contacts](/API_docs/types/contacts.Contacts.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$contacts_Contacts = $MadelineProto->contacts->getContacts(hash: [$long\|string, $long\|string], );
```

