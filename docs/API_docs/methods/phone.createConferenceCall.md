---
title: "phone.createConferenceCall"
description: "phone.createConferenceCall parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_createConferenceCall.html
---
# Method: phone.createConferenceCall
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|muted|[Bool](/API_docs/types/Bool.html) | Optional|
|video\_stopped|[Bool](/API_docs/types/Bool.html) | Optional|
|join|[Bool](/API_docs/types/Bool.html) | Optional|
|public\_key|[int256](/API_docs/types/int256.html) | Optional|
|block|[bytes](/API_docs/types/bytes.html) | Optional|
|params|[DataJSON](/API_docs/types/DataJSON.html) | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->phone->createConferenceCall(muted: $Bool, video_stopped: $Bool, join: $Bool, public_key: $int256, block: 'bytes', params: $DataJSON, );
```

