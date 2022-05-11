---
title: "contacts.getBlocked"
description: "Returns the list of blocked users."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_getBlocked.html
---
# Method: contacts.getBlocked
[Back to methods index](index.html)



Returns the list of blocked users.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|offset|[int](/API_docs/types/int.html) | The number of list elements to be skipped | Yes|
|limit|[int](/API_docs/types/int.html) | The number of list elements to be returned | Yes|


### Return type: [contacts.Blocked](/API_docs/types/contacts.Blocked.html)

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
$contacts_Blocked = $MadelineProto->contacts->getBlocked(offset: int, limit: int, );
```

