---
title: "phone.discardCall"
description: "You cannot use this method directly, see https://docs.madelineproto.xyz#calls for more info on handling calls"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_discardCall.html
---
# Method: phone.discardCall
[Back to methods index](index.html)



You cannot use this method directly, see https://docs.madelineproto.xyz#calls for more info on handling calls

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|video|[Bool](/API_docs/types/Bool.html) | Whether this is a video call | Optional|
|peer|[InputPhoneCall](/API_docs/types/InputPhoneCall.html) | The phone call | Yes|
|duration|[int](/API_docs/types/int.html) | Call duration | Yes|
|reason|[PhoneCallDiscardReason](/API_docs/types/PhoneCallDiscardReason.html) | Why was the call discarded | Yes|
|connection\_id|[long](/API_docs/types/long.html) | Preferred libtgvoip relay ID | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Updates = $MadelineProto->phone->discardCall(video: Bool, peer: InputPhoneCall, duration: int, reason: PhoneCallDiscardReason, connection_id: long, );
```

