---
title: upload.getWebFile
description: Download a file through telegram
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: upload.getWebFile  
[Back to methods index](index.md)


Download a file through telegram

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|location|[InputWebFileLocation](../types/InputWebFileLocation.md) | The file | Yes|
|offset|[int](../types/int.md) | The offset in bytes | Yes|
|limit|[int](../types/int.md) | The number of bytes to fetch | Yes|


### Return type: [upload\_WebFile](../types/upload_WebFile.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$upload_WebFile = $MadelineProto->upload->getWebFile(['location' => InputWebFileLocation, 'offset' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
upload_WebFile = upload.getWebFile({location=InputWebFileLocation, offset=int, limit=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|LOCATION_INVALID|The provided location is invalid|


