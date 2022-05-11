---
title: "upload.saveBigFilePart"
description: "You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/upload_saveBigFilePart.html
---
# Method: upload.saveBigFilePart
[Back to methods index](index.html)



You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file\_id|[long](/API_docs/types/long.html) | Random file id, created by the client | Yes|
|file\_part|[int](/API_docs/types/int.html) | Part sequence number | Yes|
|file\_total\_parts|[int](/API_docs/types/int.html) | Total number of parts | Yes|
|bytes|[bytes](/API_docs/types/bytes.html) | Binary data, part contents | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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
$Bool = $MadelineProto->upload->saveBigFilePart(file_id: long, file_part: int, file_total_parts: int, bytes: 'bytes', );
```

