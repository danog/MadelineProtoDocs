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
|api\_id|[int](/API_docs/types/int.html) | Application identifier (see. [App configuration](https://core.telegram.org/myapp)) | Optional|
|device\_model|[string](/API_docs/types/string.html) | Device model | Optional|
|system\_version|[string](/API_docs/types/string.html) | Operation system version | Optional|
|app\_version|[string](/API_docs/types/string.html) | Application version | Optional|
|system\_lang\_code|[string](/API_docs/types/string.html) | Code for the language used on the device's OS, ISO 639-1 standard | Optional|
|lang\_pack|[string](/API_docs/types/string.html) | Platform identifier (i.e. `android`, `tdesktop`, etc). | Optional|
|lang\_code|[string](/API_docs/types/string.html) | Either an ISO 639-1 language code or a language pack name obtained from a [language pack link](https://core.telegram.org/api/links#language-pack-links). | Optional|
|proxy|[InputClientProxy](/API_docs/types/InputClientProxy.html) | Info about an MTProto proxy | Optional|
|params|[JSONValue](/API_docs/types/JSONValue.html) | Additional initConnection parameters. <br>For now, only the `tz_offset` field is supported, for specifying the timezone offset in seconds. | Optional|
|query|[!X](/API_docs/types/!X.html) | The query itself | Yes|


### Return type: [X](/API_docs/types/X.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$X = $MadelineProto->initConnection(api_id: $int, device_model: 'string', system_version: 'string', app_version: 'string', system_lang_code: 'string', lang_pack: 'string', lang_code: 'string', proxy: $InputClientProxy, params: $JSONValue, query: $!X, );
```

