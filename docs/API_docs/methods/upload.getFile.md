---
title: upload.getFile
description: You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/upload_getFile.html
---
# Method: upload.getFile  
[Back to methods index](index.md)


You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|precise|[Bool](../types/Bool.md) | You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info | Optional|
|cdn\_supported|[Bool](../types/Bool.md) |  | Optional|
|location|[InputFileLocation](../types/InputFileLocation.md) | You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info | Yes|
|offset|[int](../types/int.md) | You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info | Yes|
|limit|[int](../types/int.md) | You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info | Yes|


### Return type: [upload.File](../types/upload.File.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$upload.File = $MadelineProto->upload->getFile(['precise' => Bool, 'cdn_supported' => Bool, 'location' => InputFileLocation, 'offset' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
upload.File = upload.getFile({precise=Bool, cdn_supported=Bool, location=InputFileLocation, offset=int, limit=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|FILE_ID_INVALID|The provided file id is invalid|
|400|FILE_REFERENCE_EXPIRED|File reference expired, it must be refetched as described in https://core.telegram.org/api/file_reference|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|LIMIT_INVALID|The provided limit is invalid|
|400|LOCATION_INVALID|The provided location is invalid|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|OFFSET_INVALID|The provided offset is invalid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|406|FILEREF_UPGRADE_NEEDED|The client has to be updated in order to support [file references](https://core.telegram.org/api/file_reference)|
|401|AUTH_KEY_PERM_EMPTY|The temporary auth key must be binded to the permanent auth key to use these methods.|
|-503|Timeout|Timeout while fetching data|


