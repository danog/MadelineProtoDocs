---
title: upload.reuploadCdnFile
description: Request a reupload of a certain file to a [CDN DC](https://core.telegram.org/cdn).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: upload.reuploadCdnFile  
[Back to methods index](index.md)


Request a reupload of a certain file to a [CDN DC](https://core.telegram.org/cdn).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file\_token|[bytes](../types/bytes.md) | File token | Yes|
|request\_token|[bytes](../types/bytes.md) | Request token | Yes|


### Return type: [Vector\_of\_FileHash](../types/FileHash.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_FileHash = $MadelineProto->upload->reuploadCdnFile(['file_token' => 'bytes', 'request_token' => 'bytes', ]);
```

Or, if you're into Lua:

```lua
Vector_of_FileHash = upload.reuploadCdnFile({file_token='bytes', request_token='bytes', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|RSA_DECRYPT_FAILED|Internal RSA decryption failed|


