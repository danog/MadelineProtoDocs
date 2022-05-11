---
title: "contacts.getContactIDs"
description: "Get contact by telegram IDs"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_getContactIDs.html
---
# Method: contacts.getContactIDs
[Back to methods index](index.html)



Get contact by telegram IDs

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|[long](/API_docs/types/long.html) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Yes|


### Return type: [Vector\_of\_int](/API_docs/types/int.html)

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
$Vector_of_int = $MadelineProto->contacts->getContactIDs(hash: long, );
```

