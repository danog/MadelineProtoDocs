---
title: messages.getDocumentByHash
description: Get document by SHA256 hash
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getDocumentByHash  
[Back to methods index](index.md)


Get document by SHA256 hash

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|sha256|[bytes](../types/bytes.md) | `hash('sha256', $filename, true);` | Yes|
|size|[int](../types/int.md) | The file size | Yes|
|mime\_type|[string](../types/string.md) | The mime type of the file | Yes|


### Return type: [Document](../types/Document.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Document = $MadelineProto->messages->getDocumentByHash(['sha256' => 'bytes', 'size' => int, 'mime_type' => 'string', ]);
```

Or, if you're into Lua:

```lua
Document = messages.getDocumentByHash({sha256='bytes', size=int, mime_type='string', })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|SHA256_HASH_INVALID|The provided SHA256 hash is invalid|


