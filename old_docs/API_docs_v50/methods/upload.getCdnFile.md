---
title: upload.getCdnFile
description: Download a [CDN](https://core.telegram.org/cdn) file.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/upload_getCdnFile.html
---
# Method: upload.getCdnFile
[Back to methods index](index.md)



Download a [CDN](https://core.telegram.org/cdn) file.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file\_token|[bytes](../types/bytes.md) | File token | Yes|
|offset|[int](../types/int.md) | Offset of chunk to download | Yes|
|limit|[int](../types/int.md) | Length of chunk to download | Yes|


### Return type: [upload.CdnFile](../types/upload.CdnFile.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$upload_CdnFile = $MadelineProto->upload->getCdnFile(['file_token' => 'bytes', 'offset' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
upload_CdnFile = upload.getCdnFile({file_token='bytes', offset=int, limit=int, })
```

