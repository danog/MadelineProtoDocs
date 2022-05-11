---
title: "upload.getWebFile"
description: "Returns content of an HTTP file or a part, by proxying the request through telegram."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/upload_getWebFile.html
---
# Method: upload.getWebFile
[Back to methods index](index.html)



Returns content of an HTTP file or a part, by proxying the request through telegram.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|location|[InputWebFileLocation](/API_docs/types/InputWebFileLocation.html) | The file to download | Yes|
|offset|[int](/API_docs/types/int.html) | Number of bytes to be skipped | Yes|
|limit|[int](/API_docs/types/int.html) | Number of bytes to be returned | Yes|


### Return type: [upload.WebFile](/API_docs/types/upload.WebFile.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$upload_WebFile = $MadelineProto->upload->getWebFile(location: InputWebFileLocation, offset: int, limit: int, );
```

