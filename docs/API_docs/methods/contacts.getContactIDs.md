---
title: "contacts.getContactIDs"
description: "Get the telegram IDs of all contacts.  "
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_getContactIDs.html
---
# Method: contacts.getContactIDs
[Back to methods index](index.html)



Get the telegram IDs of all contacts.  
Returns an array of Telegram user IDs for all contacts (0 if a contact does not have an associated Telegram account or have hidden their account using privacy settings).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [Vector\_of\_int](/API_docs/types/int.html)

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

$Vector_of_int = $MadelineProto->contacts->getContactIDs(hash: [$long\|string, $long\|string], );
```

