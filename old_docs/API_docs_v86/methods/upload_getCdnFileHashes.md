---
title: upload.getCdnFileHashes
description: You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: upload.getCdnFileHashes  
[Back to methods index](index.md)


You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file\_token|[bytes](../types/bytes.md) | You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info | Yes|
|offset|[int](../types/int.md) | You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info | Yes|


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


