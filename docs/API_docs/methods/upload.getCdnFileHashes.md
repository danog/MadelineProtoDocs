---
title: "upload.getCdnFileHashes"
description: "Get SHA256 hashes for verifying downloaded [CDN](https://core.telegram.org/cdn) files"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/upload_getCdnFileHashes.html
---
# Method: upload.getCdnFileHashes
[Back to methods index](index.md)



Get SHA256 hashes for verifying downloaded [CDN](https://core.telegram.org/cdn) files

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file\_token|[bytes](../types/bytes.md) | File | Yes|
|offset|[int](../types/int.md) | Offset from which to start getting hashes | Yes|


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

$Vector_of_FileHash = $MadelineProto->upload->getCdnFileHashes(['file_token' => 'bytes', 'offset' => int, ]);
```

Or, if you're into Lua:

```lua
Vector_of_FileHash = upload.getCdnFileHashes({file_token='bytes', offset=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CDN_METHOD_INVALID|You can't call this method in a CDN DC|
|400|RSA_DECRYPT_FAILED|Internal RSA decryption failed|


