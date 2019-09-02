---
title: upload.getFile
description: You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: upload.getFile  
[Back to methods index](index.md)


You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|location|[InputFileLocation](../types/InputFileLocation.md) | You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info | Yes|
|offset|[int](../types/int.md) | You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info | Yes|
|limit|[int](../types/int.md) | You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info | Yes|


### Return type: [upload\_File](../types/upload_File.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$upload_File = $MadelineProto->upload->getFile(['location' => InputFileLocation, 'offset' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
upload_File = upload.getFile({location=InputFileLocation, offset=int, limit=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|FILE_ID_INVALID|The provided file id is invalid|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|LIMIT_INVALID|The provided limit is invalid|
|400|LOCATION_INVALID|The provided location is invalid|
|400|OFFSET_INVALID|The provided offset is invalid|
|401|AUTH_KEY_PERM_EMPTY|The temporary auth key must be binded to the permanent auth key to use these methods.|
|-503|Timeout|Timeout while fetching data|


