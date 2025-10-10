---
title: "phone.toggleGroupCallSettings"
description: "Change group call settings"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_toggleGroupCallSettings.html
---
# Method: phone.toggleGroupCallSettings
[Back to methods index](index.html)



Change group call settings

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|reset\_invite\_hash|[Bool](/API_docs/types/Bool.html) | Invalidate existing invite links | Optional|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Group call | Yes|
|join\_muted|[Bool](/API_docs/types/Bool.html) | Whether all users will that join this group call are muted by default upon joining the group call | Optional|
|messages\_enabled|[Bool](/API_docs/types/Bool.html) |  | Optional|


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

$Updates = $MadelineProto->phone->toggleGroupCallSettings(reset_invite_hash: $Bool, call: $InputGroupCall, join_muted: $Bool, messages_enabled: $Bool, );
```

