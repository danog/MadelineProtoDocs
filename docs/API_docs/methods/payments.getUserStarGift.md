---
title: "payments.getUserStarGift"
description: "payments.getUserStarGift parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getUserStarGift.html
---
# Method: payments.getUserStarGift
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|msg\_id|Array of [int](/API_docs/types/int.html) | Yes|


### Return type: [payments.UserStarGifts](/API_docs/types/payments.UserStarGifts.html)

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

$payments_UserStarGifts = $MadelineProto->payments->getUserStarGift(msg_id: [$int, $int], );
```

