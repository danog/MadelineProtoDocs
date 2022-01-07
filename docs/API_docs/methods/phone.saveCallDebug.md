---
title: "phone.saveCallDebug"
description: "Send phone call debug data to server"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_saveCallDebug.html
---
# Method: phone.saveCallDebug
[Back to methods index](index.md)



Send phone call debug data to server

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[InputPhoneCall](../types/InputPhoneCall.md) | Phone call | Yes|
|debug|[DataJSON](../types/DataJSON.md) | Debug statistics obtained from libtgvoip | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->phone->saveCallDebug(['peer' => InputPhoneCall, 'debug' => DataJSON, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CALL_PEER_INVALID|The provided call peer object is invalid|
|400|DATA_JSON_INVALID|The provided JSON data is invalid|


