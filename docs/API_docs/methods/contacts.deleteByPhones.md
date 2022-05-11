---
title: "contacts.deleteByPhones"
description: "Delete contacts by phone number"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_deleteByPhones.html
---
# Method: contacts.deleteByPhones
[Back to methods index](index.html)



Delete contacts by phone number

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phones|Array of [string](/API_docs/types/string.html) | Phone numbers | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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
$Bool = $MadelineProto->contacts->deleteByPhones(phones: ['string', 'string'], );
```

