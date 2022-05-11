---
title: "auth.exportAuthorization"
description: "You cannot use this method directly, use $MadelineProto->exportAuthorization() instead, see https://docs.madelineproto.xyz/docs/LOGIN.html"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_exportAuthorization.html
---
# Method: auth.exportAuthorization
[Back to methods index](index.html)



You cannot use this method directly, use $MadelineProto->exportAuthorization() instead, see https://docs.madelineproto.xyz/docs/LOGIN.html

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|dc\_id|[int](/API_docs/types/int.html) | Number of a target data-center | Yes|


### Return type: [auth.ExportedAuthorization](/API_docs/types/auth.ExportedAuthorization.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$auth_ExportedAuthorization = $MadelineProto->auth->exportAuthorization(dc_id: int, );
```

