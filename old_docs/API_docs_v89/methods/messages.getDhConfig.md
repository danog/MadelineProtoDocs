---
title: messages.getDhConfig
description: You cannot use this method directly, instead use $MadelineProto->getDhConfig();
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getDhConfig  
[Back to methods index](index.md)


You cannot use this method directly, instead use $MadelineProto->getDhConfig();

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|version|[int](../types/int.md) | You cannot use this method directly, instead use $MadelineProto->getDhConfig(); | Yes|
|random\_length|[int](../types/int.md) | You cannot use this method directly, instead use $MadelineProto->getDhConfig(); | Yes|


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

$messages.DhConfig = $MadelineProto->messages->getDhConfig(['version' => int, 'random_length' => int, ]);
```

Or, if you're into Lua:

```lua
messages.DhConfig = messages.getDhConfig({version=int, random_length=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|RANDOM_LENGTH_INVALID|Random length invalid|


