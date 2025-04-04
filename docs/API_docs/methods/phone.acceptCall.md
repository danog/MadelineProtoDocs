---
title: "phone.acceptCall"
description: "You cannot use this method directly, see https://docs.madelineproto.xyz#calls for more info on handling calls"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_acceptCall.html
---
# Method: phone.acceptCall
[Back to methods index](index.html)



You cannot use this method directly, see https://docs.madelineproto.xyz#calls for more info on handling calls

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[InputPhoneCall](/API_docs/types/InputPhoneCall.html) | The call to accept | Yes|
|g\_b|[bytes](/API_docs/types/bytes.html) | [Parameter for E2E encryption key exchange »](https://core.telegram.org/api/end-to-end/voice-calls) | Yes|
|protocol|[PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.html) | Phone call settings | Yes|


### Return type: [phone.PhoneCall](/API_docs/types/phone.PhoneCall.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$phone_PhoneCall = $MadelineProto->phone->acceptCall(peer: $InputPhoneCall, g_b: 'bytes', protocol: $PhoneCallProtocol, );
```

