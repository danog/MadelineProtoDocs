---
title: "payments.getStarsSubscriptions"
description: "payments.getStarsSubscriptions parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getStarsSubscriptions.html
---
# Method: payments.getStarsSubscriptions
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|missing\_balance|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|offset|[string](/API_docs/types/string.html) | Optional|


### Return type: [payments.StarsStatus](/API_docs/types/payments.StarsStatus.html)

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

$payments_StarsStatus = $MadelineProto->payments->getStarsSubscriptions(missing_balance: $Bool, peer: $InputPeer, offset: 'string', );
```

