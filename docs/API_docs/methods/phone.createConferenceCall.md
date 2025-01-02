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
|peer|[InputPhoneCall](/API_docs/types/InputPhoneCall.html) | Yes|
|key\_fingerprint|[strlong](/API_docs/constructors/strlong.html) | Yes|


### Return type: [phone.PhoneCall](/API_docs/types/phone.PhoneCall.html)

### Can userbots use this method: **YES**

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$phone_PhoneCall = $MadelineProto->phone->createConferenceCall(peer: $InputPhoneCall, key_fingerprint: $strlong, );
```

