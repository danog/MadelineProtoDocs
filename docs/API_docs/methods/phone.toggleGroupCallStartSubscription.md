---
title: "phone.toggleGroupCallStartSubscription"
description: "Subscribe or unsubscribe to a scheduled group call"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_toggleGroupCallStartSubscription.html
---
# Method: phone.toggleGroupCallStartSubscription
[Back to methods index](index.html)



Subscribe or unsubscribe to a scheduled group call

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Scheduled group call | Yes|
|subscribed|[Bool](/API_docs/types/Bool.html) | Enable or disable subscription | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->phone->toggleGroupCallStartSubscription(call: $InputGroupCall, subscribed: $Bool, );
```

