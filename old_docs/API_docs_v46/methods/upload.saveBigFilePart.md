---
title: upload.saveBigFilePart
description: Saves a part of a large file (over 10Mb in size) to be later passed to one of the methods.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/upload_saveBigFilePart.html
---
# Method: upload.saveBigFilePart
[Back to methods index](index.md)



Saves a part of a large file (over 10Mb in size) to be later passed to one of the methods.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file\_id|[long](../types/long.md) | Random file id, created by the client | Yes|
|file\_part|[int](../types/int.md) | Part sequence number | Yes|
|file\_total\_parts|[int](../types/int.md) | Total number of parts | Yes|
|bytes|[bytes](../types/bytes.md) | Binary data, part contents | Yes|


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

$Bool = $MadelineProto->upload->saveBigFilePart(['file_id' => long, 'file_part' => int, 'file_total_parts' => int, 'bytes' => 'bytes', ]);
```

Or, if you're into Lua:

```lua
Bool = upload.saveBigFilePart({file_id=long, file_part=int, file_total_parts=int, bytes='bytes', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|FILE_PART_EMPTY|The provided file part is empty|
|400|FILE_PART_INVALID|The file part number is invalid|
|400|FILE_PART_SIZE_CHANGED|Provided file part size has changed|
|400|FILE_PART_SIZE_INVALID|The provided file part size is invalid|
|400|FILE_PART_TOO_BIG|The uploaded file part is too big|
|400|FILE_PARTS_INVALID|The number of file parts is invalid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|-503|Timeout|Timeout while fetching data|


