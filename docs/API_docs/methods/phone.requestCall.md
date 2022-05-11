---
title: "phone.requestCall"
description: "You cannot use this method directly, see https://docs.madelineproto.xyz#calls for more info on handling calls"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_requestCall.html
---
# Method: phone.requestCall
[Back to methods index](index.html)



You cannot use this method directly, see https://docs.madelineproto.xyz#calls for more info on handling calls

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|video|[Bool](/API_docs/types/Bool.html) | Whether to start a video call | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Destination of the phone call | Optional|
|g\_a\_hash|[bytes](/API_docs/types/bytes.html) | [Parameter for E2E encryption key exchange »](https://core.telegram.org/api/end-to-end/voice-calls) | Yes|
|protocol|[PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.html) | Phone call settings | Yes|


### Return type: [phone.PhoneCall](/API_docs/types/phone.PhoneCall.html)

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
$phone_PhoneCall = $MadelineProto->phone->requestCall(video: Bool, user_id: InputUser, g_a_hash: 'bytes', protocol: PhoneCallProtocol, );
```

