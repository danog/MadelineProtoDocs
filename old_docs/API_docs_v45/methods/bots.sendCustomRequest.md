---
title: bots.sendCustomRequest
description: Sends a custom request; for bots only
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_sendCustomRequest.html
---
# Method: bots.sendCustomRequest
[Back to methods index](index.md)



Sends a custom request; for bots only

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|custom\_method|[string](../types/string.md) | The method name | Yes|
|params|[DataJSON](../types/DataJSON.md) | JSON-serialized method parameters | Yes|


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

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|METHOD_INVALID|The specified method is invalid|
|400|USER_BOT_INVALID|This method can only be called by a bot|


