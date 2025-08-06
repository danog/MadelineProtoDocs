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
|q|[string](/API_docs/types/string.html) | Target substring | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of users to be returned | Optional|


### Return type: [contacts.Found](/API_docs/types/contacts.Found.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$contacts_Found = $MadelineProto->contacts->search(q: 'string', limit: $int, );
```

