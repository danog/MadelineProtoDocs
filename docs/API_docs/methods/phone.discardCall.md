---
title: "phone.discardCall"
description: "You cannot use this method directly, see https://docs.madelineproto.xyz#calls for more info on handling calls"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_discardCall.html
---
# Method: phone.discardCall
[Back to methods index](index.md)



You cannot use this method directly, see https://docs.madelineproto.xyz#calls for more info on handling calls

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|video|[Bool](../types/Bool.md) | Whether this is a video call | Optional|
|peer|[InputPhoneCall](../types/InputPhoneCall.md) | The phone call | Yes|
|duration|[int](../types/int.md) | Call duration | Yes|
|reason|[PhoneCallDiscardReason](../types/PhoneCallDiscardReason.md) | Why was the call discarded | Yes|
|connection\_id|[long](../types/long.md) | Preferred libtgvoip relay ID | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->phone->discardCall(['video' => Bool, 'peer' => InputPhoneCall, 'duration' => int, 'reason' => PhoneCallDiscardReason, 'connection_id' => long, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CALL_ALREADY_ACCEPTED|The call was already accepted|
|400|CALL_PEER_INVALID|The provided call peer object is invalid|


