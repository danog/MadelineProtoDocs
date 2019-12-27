---
title: upload.getFileHashes
description: Get SHA256 hashes for verifying downloaded files
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: upload.getFileHashes  
[Back to methods index](index.md)


Get SHA256 hashes for verifying downloaded files

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|location|[InputFileLocation](../types/InputFileLocation.md) | File | Yes|
|offset|[int](../types/int.md) | Offset from which to get file hashes | Yes|


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


