---
title: "messages.getDhConfig"
description: "You cannot use this method directly, instead use $MadelineProto->getDhConfig();"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getDhConfig.html
---
# Method: messages.getDhConfig
[Back to methods index](index.html)



You cannot use this method directly, instead use $MadelineProto->getDhConfig();

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|version|[int](/API_docs/types/int.html) | Value of the **version** parameter from [messages.dhConfig](../constructors/messages.dhConfig.html), available at the client | Yes|
|random\_length|[int](/API_docs/types/int.html) | Length of the required random sequence | Yes|


### Return type: [messages.DhConfig](/API_docs/types/messages.DhConfig.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$messages_DhConfig = $MadelineProto->messages->getDhConfig(version: int, random_length: int, );
```

