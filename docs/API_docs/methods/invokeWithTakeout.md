---
title: "invokeWithTakeout"
description: "Invoke a method within a takeout session"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: invokeWithTakeout
[Back to methods index](index.html)



Invoke a method within a takeout session

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|takeout\_id|[long](/API_docs/types/long.html) | Takeout session ID | Yes|
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
$X = $MadelineProto->invokeWithTakeout(takeout_id: long, query: !X, );
```

