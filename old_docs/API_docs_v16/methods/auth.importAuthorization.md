---
title: auth.importAuthorization
description: Logs in a user using a key transmitted from his native data-centre.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_importAuthorization.html
---
# Method: auth.importAuthorization
[Back to methods index](index.md)



Logs in a user using a key transmitted from his native data-centre.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[int](../types/int.md) | User ID | Yes|
|bytes|[bytes](../types/bytes.md) | Authorization key | Yes|


### Return type: [auth.Authorization](../types/auth.Authorization.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth.Authorization = $MadelineProto->auth->importAuthorization(['id' => int, 'bytes' => 'bytes', ]);
```

Or, if you're into Lua:

```lua
auth.Authorization = auth.importAuthorization({id=int, bytes='bytes', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|AUTH_BYTES_INVALID|The provided authorization is invalid|
|400|USER_ID_INVALID|The provided user ID is invalid|


