---
title: upload.getWebFile
description: Returns content of an HTTP file or a part, by proxying the request through telegram.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/upload_getWebFile.html
---
# Method: upload.getWebFile
[Back to methods index](index.md)



Returns content of an HTTP file or a part, by proxying the request through telegram.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|location|[InputWebFileLocation](../types/InputWebFileLocation.md) | The file to download | Yes|
|offset|[int](../types/int.md) | Number of bytes to be skipped | Yes|
|limit|[int](../types/int.md) | Number of bytes to be returned | Yes|


### Return type: [upload.WebFile](../types/upload.WebFile.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$upload_WebFile = $MadelineProto->upload->getWebFile(['location' => InputWebFileLocation, 'offset' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
upload_WebFile = upload.getWebFile({location=InputWebFileLocation, offset=int, limit=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|LOCATION_INVALID|The provided location is invalid|


