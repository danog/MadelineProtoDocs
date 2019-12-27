---
title: upload.reuploadCdnFile
description: You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/upload_reuploadCdnFile.html
---
# Method: upload.reuploadCdnFile  
[Back to methods index](index.md)


You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file\_token|[bytes](../types/bytes.md) | You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info | Yes|
|request\_token|[bytes](../types/bytes.md) | You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->upload->reuploadCdnFile(['file_token' => 'bytes', 'request_token' => 'bytes', ]);
```

Or, if you're into Lua:

```lua
Bool = upload.reuploadCdnFile({file_token='bytes', request_token='bytes', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|RSA_DECRYPT_FAILED|Internal RSA decryption failed|


