---
title: "upload.getFile"
description: "You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/upload_getFile.html
---
# Method: upload.getFile
[Back to methods index](index.html)



You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|precise|[Bool](/API_docs/types/Bool.html) | Disable some checks on limit and offset values, useful for example to stream videos by keyframes | Optional|
|cdn\_supported|[Bool](/API_docs/types/Bool.html) | Whether the current client supports [CDN downloads](https://core.telegram.org/cdn) | Optional|
|location|[InputFileLocation](/API_docs/types/InputFileLocation.html) | File location | Yes|
|offset|[long](/API_docs/types/long.html) |  | Yes|
|limit|[int](/API_docs/types/int.html) | Number of bytes to be returned | Yes|


### Return type: [upload.File](/API_docs/types/upload.File.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$upload_File = $MadelineProto->upload->getFile(precise: Bool, cdn_supported: Bool, location: InputFileLocation, offset: long, limit: int, );
```

