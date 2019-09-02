---
title: upload.getCdnFile
description: You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: upload.getCdnFile  
[Back to methods index](index.md)


You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file\_token|[bytes](../types/bytes.md) | You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info | Yes|
|offset|[int](../types/int.md) | You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info | Yes|
|limit|[int](../types/int.md) | You cannot use this method directly, use the upload, download_to_stream, download_to_file, download_to_dir methods instead; see https://docs.madelineproto.xyz for more info | Yes|


### Return type: [upload\_CdnFile](../types/upload_CdnFile.md)

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

