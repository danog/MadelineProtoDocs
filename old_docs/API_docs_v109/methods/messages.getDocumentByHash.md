---
title: messages.getDocumentByHash
description: Get a document by its SHA256 hash, mainly used for gifs
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getDocumentByHash.html
---
# Method: messages.getDocumentByHash  
[Back to methods index](index.md)


Get a document by its SHA256 hash, mainly used for gifs

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|sha256|[bytes](../types/bytes.md) | SHA256 of file | Yes|
|size|[int](../types/int.md) | Size of the file in bytes | Yes|
|mime\_type|[string](../types/string.md) | Mime type | Yes|


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

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|SHA256_HASH_INVALID|The provided SHA256 hash is invalid|


