---
title: upload.saveFilePart
description: You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: upload.saveFilePart  
[Back to methods index](index.md)


You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file\_id|[long](../types/long.md) | You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info | Yes|
|file\_part|[int](../types/int.md) | You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info | Yes|
|bytes|[bytes](../types/bytes.md) | You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info | Yes|


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

$Bool = $MadelineProto->upload->saveFilePart(['file_id' => long, 'file_part' => int, 'bytes' => 'bytes', ]);
```

Or, if you're into Lua:

```lua
Bool = upload.saveFilePart({file_id=long, file_part=int, bytes='bytes', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|FILE_PART_EMPTY|The provided file part is empty|
|400|FILE_PART_INVALID|The file part number is invalid|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|


