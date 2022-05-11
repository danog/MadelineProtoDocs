---
title: "initConnection"
description: "Initialize connection"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: initConnection
[Back to methods index](index.html)



Initialize connection

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|api\_id|[int](/API_docs/types/int.html) | Application identifier (see. [App configuration](https://core.telegram.org/myapp)) | Yes|
|device\_model|[string](/API_docs/types/string.html) | Device model | Yes|
|system\_version|[string](/API_docs/types/string.html) | Operation system version | Yes|
|app\_version|[string](/API_docs/types/string.html) | Application version | Yes|
|system\_lang\_code|[string](/API_docs/types/string.html) | Code for the language used on the device's OS, ISO 639-1 standard | Yes|
|lang\_pack|[string](/API_docs/types/string.html) | Language pack to use | Yes|
|lang\_code|[string](/API_docs/types/string.html) | Code for the language used on the client, ISO 639-1 standard | Yes|
|proxy|[InputClientProxy](/API_docs/types/InputClientProxy.html) | Info about an MTProto proxy | Optional|
|params|[JSONValue](/API_docs/types/JSONValue.html) | Additional initConnection parameters. <br>For now, only the `tz_offset` field is supported, for specifying timezone offset in seconds. | Optional|
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
$X = $MadelineProto->initConnection(api_id: int, device_model: 'string', system_version: 'string', app_version: 'string', system_lang_code: 'string', lang_pack: 'string', lang_code: 'string', proxy: InputClientProxy, params: JSONValue, query: !X, );
```

