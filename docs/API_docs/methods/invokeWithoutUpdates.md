---
title: "invokeWithoutUpdates"
description: "Invoke a request without subscribing the used connection for [updates](https://core.telegram.org/api/updates) (this is enabled by default for [file queries](https://core.telegram.org/api/files))."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: invokeWithoutUpdates
[Back to methods index](index.html)



Invoke a request without subscribing the used connection for [updates](https://core.telegram.org/api/updates) (this is enabled by default for [file queries](https://core.telegram.org/api/files)).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
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
$X = $MadelineProto->invokeWithoutUpdates(query: !X, );
```

