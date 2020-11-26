---
title: initConnection
description: Initialize connection
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: initConnection
[Back to methods index](index.md)



Initialize connection

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|api\_id|[int](../types/int.md) | Application identifier (see. [App configuration](https://core.telegram.org/myapp)) | Yes|
|device\_model|[string](../types/string.md) | Device model | Yes|
|system\_version|[string](../types/string.md) | Operation system version | Yes|
|app\_version|[string](../types/string.md) | Application version | Yes|
|system\_lang\_code|[string](../types/string.md) | Code for the language used on the device's OS, ISO 639-1 standard | Yes|
|lang\_pack|[string](../types/string.md) | Language pack to use | Yes|
|lang\_code|[string](../types/string.md) | Code for the language used on the client, ISO 639-1 standard | Yes|
|proxy|[InputClientProxy](../types/InputClientProxy.md) | Info about an MTProto proxy | Optional|
|params|[JSONValue](../types/JSONValue.md) | Additional initConnection parameters. <br>For now, only the `tz_offset` field is supported, for specifying timezone offset in seconds. | Optional|
|query|[!X](../types/!X.md) | The query itself | Yes|


### Return type: [X](../types/X.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$X = $MadelineProto->initConnection(['api_id' => int, 'device_model' => 'string', 'system_version' => 'string', 'app_version' => 'string', 'system_lang_code' => 'string', 'lang_pack' => 'string', 'lang_code' => 'string', 'proxy' => InputClientProxy, 'params' => JSONValue, 'query' => !X, ]);
```

Or, if you're into Lua:

```lua
X = initConnection({api_id=int, device_model='string', system_version='string', app_version='string', system_lang_code='string', lang_pack='string', lang_code='string', proxy=InputClientProxy, params=JSONValue, query=!X, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CONNECTION_LAYER_INVALID|Layer invalid|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|


