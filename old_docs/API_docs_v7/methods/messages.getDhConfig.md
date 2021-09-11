---
title: messages.getDhConfig
description: Returns configuration parameters for Diffie-Hellman key generation. Can also return a random sequence of bytes of required length.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getDhConfig.html
---
# Method: messages.getDhConfig
[Back to methods index](index.md)



Returns configuration parameters for Diffie-Hellman key generation. Can also return a random sequence of bytes of required length.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|version|[int](../types/int.md) | Value of the **version** parameter from [messages.dhConfig](../constructors/messages.dhConfig.md), avialable at the client | Yes|
|random\_length|[int](../types/int.md) | Length of the required random sequence | Yes|


### Return type: [messages.DhConfig](../types/messages.DhConfig.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_DhConfig = $MadelineProto->messages->getDhConfig(['version' => int, 'random_length' => int, ]);
```

Or, if you're into Lua:

```lua
messages_DhConfig = messages.getDhConfig({version=int, random_length=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|RANDOM_LENGTH_INVALID|Random length invalid|
|-503|Timeout|Timeout while fetching data|


