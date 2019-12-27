---
title: upload.getFileHashes
description: You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/upload_getFileHashes.html
---
# Method: upload.getFileHashes  
[Back to methods index](index.md)


You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|location|[InputFileLocation](../types/InputFileLocation.md) | You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info | Yes|
|offset|[int](../types/int.md) | You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info | Yes|


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

$Vector_of_FileHash = $MadelineProto->upload->getFileHashes(['location' => InputFileLocation, 'offset' => int, ]);
```

Or, if you're into Lua:

```lua
Vector_of_FileHash = upload.getFileHashes({location=InputFileLocation, offset=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|LOCATION_INVALID|The provided location is invalid|


