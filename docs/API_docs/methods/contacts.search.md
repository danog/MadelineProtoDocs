---
title: "contacts.search"
description: "Returns users found by username substring."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_search.html
---
# Method: contacts.search
[Back to methods index](index.html)



Returns users found by username substring.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|q|[string](/API_docs/types/string.html) | Target substring | Yes|
|limit|[int](/API_docs/types/int.html) | Maximum number of users to be returned | Yes|


### Return type: [contacts.Found](/API_docs/types/contacts.Found.html)

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
$contacts_Found = $MadelineProto->contacts->search(q: 'string', limit: int, );
```

