---
title: "messages.getDocumentByHash"
description: "Get a document by its SHA256 hash, mainly used for gifs"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getDocumentByHash.html
---
# Method: messages.getDocumentByHash
[Back to methods index](index.html)



Get a document by its SHA256 hash, mainly used for gifs

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|sha256|[bytes](/API_docs/types/bytes.html) | SHA256 of file | Yes|
|size|[long](/API_docs/types/long.html) |  | Yes|
|mime\_type|[string](/API_docs/types/string.html) | Mime type | Yes|


### Return type: [Document](/API_docs/types/Document.html)

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
$Document = $MadelineProto->messages->getDocumentByHash(sha256: 'bytes', size: long, mime_type: 'string', );
```

