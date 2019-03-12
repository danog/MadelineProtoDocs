---
title: initConnection
description: Initializes connection and save information on the user's device and application.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: initConnection  
[Back to methods index](index.md)


Initializes connection and save information on the user's device and application.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|api\_id|[int](../types/int.md) | Application identifier | Yes|
|device\_model|[string](../types/string.md) | Device model | Yes|
|system\_version|[string](../types/string.md) | System version | Yes|
|app\_version|[string](../types/string.md) | App version | Yes|
|system\_lang\_code|[string](../types/string.md) | Language code | Yes|
|lang\_pack|[string](../types/string.md) | Language pack to use | Yes|
|lang\_code|[string](../types/string.md) | Language code to set | Yes|
|proxy|[InputClientProxy](../types/InputClientProxy.md) | The current proxy | Optional|
|query|[!X](../types/!X.md) | Nested query | Yes|


### Return type: [X](../types/X.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$X = $MadelineProto->initConnection(['api_id' => int, 'device_model' => 'string', 'system_version' => 'string', 'app_version' => 'string', 'system_lang_code' => 'string', 'lang_pack' => 'string', 'lang_code' => 'string', 'proxy' => InputClientProxy, 'query' => !X, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - initConnection
* params - `{"api_id": int, "device_model": "string", "system_version": "string", "app_version": "string", "system_lang_code": "string", "lang_pack": "string", "lang_code": "string", "proxy": InputClientProxy, "query": !X, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/initConnection`

Parameters:

api_id - Json encoded int

device_model - Json encoded string

system_version - Json encoded string

app_version - Json encoded string

system_lang_code - Json encoded string

lang_pack - Json encoded string

lang_code - Json encoded string

proxy - Json encoded InputClientProxy

query - Json encoded !X




Or, if you're into Lua:

```lua
X = initConnection({api_id=int, device_model='string', system_version='string', app_version='string', system_lang_code='string', lang_pack='string', lang_code='string', proxy=InputClientProxy, query=!X, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CONNECTION_LAYER_INVALID|Layer invalid|
|INPUT_FETCH_FAIL|Failed deserializing TL payload|


