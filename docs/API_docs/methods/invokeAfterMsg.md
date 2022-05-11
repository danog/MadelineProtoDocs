---
title: "invokeAfterMsg"
description: "Invokes a query after successful completion of one of the previous queries."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: invokeAfterMsg
[Back to methods index](index.html)



Invokes a query after successful completion of one of the previous queries.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|msg\_id|[long](/API_docs/types/long.html) | Message identifier on which a current query depends | Yes|
|query|[!X](/API_docs/types/!X.html) | The query itself | Yes|


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
$X = $MadelineProto->invokeAfterMsg(msg_id: long, query: !X, );
```

