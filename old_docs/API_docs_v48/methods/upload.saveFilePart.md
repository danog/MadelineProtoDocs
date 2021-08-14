---
title: upload.saveFilePart
description: Saves a part of file for futher sending to one of the methods.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/upload_saveFilePart.html
---
# Method: upload.saveFilePart
[Back to methods index](index.md)



Saves a part of file for futher sending to one of the methods.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file\_id|[long](../types/long.md) | Random file identifier created by the client | Yes|
|file\_part|[int](../types/int.md) | Numerical order of a part | Yes|
|bytes|[bytes](../types/bytes.md) | Binary data, contend of a part | Yes|


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
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|
|-503|Timeout|Timeout while fetching data|


