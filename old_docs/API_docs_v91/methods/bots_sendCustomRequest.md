---
title: bots.sendCustomRequest
description: Send a custom request to the bot API
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: bots.sendCustomRequest  
[Back to methods index](index.md)


Send a custom request to the bot API

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|custom\_method|[string](../types/string.md) | The method to call | Yes|
|params|[DataJSON](../types/DataJSON.md) | Method parameters | Yes|


### Return type: [DataJSON](../types/DataJSON.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$DataJSON = $MadelineProto->bots->sendCustomRequest(['custom_method' => 'string', 'params' => DataJSON, ]);
```

Or, if you're into Lua:

```lua
DataJSON = bots.sendCustomRequest({custom_method='string', params=DataJSON, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|USER_BOT_INVALID|This method can only be called by a bot|


