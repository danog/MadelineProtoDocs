---
title: "phone.sendSignalingData"
description: "Send VoIP signaling data"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_sendSignalingData.html
---
# Method: phone.sendSignalingData
[Back to methods index](index.html)



Send VoIP signaling data

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[InputPhoneCall](/API_docs/types/InputPhoneCall.html) | Phone call | Yes|
|data|[bytes](/API_docs/types/bytes.html) | Signaling payload | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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
$Bool = $MadelineProto->phone->sendSignalingData(peer: InputPhoneCall, data: 'bytes', );
```

