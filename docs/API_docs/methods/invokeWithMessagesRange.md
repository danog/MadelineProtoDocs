---
title: "invokeWithMessagesRange"
description: "Invoke with the given message range"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: invokeWithMessagesRange
[Back to methods index](index.html)



Invoke with the given message range

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|range|[MessageRange](/API_docs/types/MessageRange.html) | Message range | Yes|
|query|[!X](/API_docs/types/!X.html) | Query | Yes|


### Return type: [X](/API_docs/types/X.html)

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
$X = $MadelineProto->invokeWithMessagesRange(range: MessageRange, query: !X, );
```

