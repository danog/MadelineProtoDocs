---
title: "upload.getCdnFile"
description: "You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/upload_getCdnFile.html
---
# Method: upload.getCdnFile
[Back to methods index](index.html)



You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file\_token|[bytes](/API_docs/types/bytes.html) | File token | Yes|
|offset|[long](/API_docs/types/long.html) |  | Yes|
|limit|[int](/API_docs/types/int.html) | Length of chunk to download | Yes|


### Return type: [upload.CdnFile](/API_docs/types/upload.CdnFile.html)

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
$upload_CdnFile = $MadelineProto->upload->getCdnFile(file_token: 'bytes', offset: long, limit: int, );
```

