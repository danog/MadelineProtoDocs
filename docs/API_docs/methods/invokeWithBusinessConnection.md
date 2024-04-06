---
title: "invokeWithBusinessConnection"
description: "invokeWithBusinessConnection parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: invokeWithBusinessConnection
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|connection\_id|[string](/API_docs/types/string.html) | Optional|
|query|[!X](/API_docs/types/!X.html) | Yes|


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

$X = $MadelineProto->invokeWithBusinessConnection(connection_id: 'string', query: $!X, );
```

