---
title: "invokeWithLayer"
description: "Invoke the specified query using the specified API [layer](https://core.telegram.org/api/invoking#layers)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: invokeWithLayer
[Back to methods index](index.html)



Invoke the specified query using the specified API [layer](https://core.telegram.org/api/invoking#layers)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|layer|[int](/API_docs/types/int.html) | The layer to use | Yes|
|query|[!X](/API_docs/types/!X.html) | The query | Yes|


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
$X = $MadelineProto->invokeWithLayer(layer: int, query: !X, );
```

