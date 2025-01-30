---
title: "payments.getSavedStarGifts"
description: "payments.getSavedStarGifts parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getSavedStarGifts.html
---
# Method: payments.getSavedStarGifts
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|exclude\_unsaved|[Bool](/API_docs/types/Bool.html) | Optional|
|exclude\_saved|[Bool](/API_docs/types/Bool.html) | Optional|
|exclude\_unlimited|[Bool](/API_docs/types/Bool.html) | Optional|
|exclude\_limited|[Bool](/API_docs/types/Bool.html) | Optional|
|exclude\_unique|[Bool](/API_docs/types/Bool.html) | Optional|
|sort\_by\_value|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|offset|[string](/API_docs/types/string.html) | Optional|
|limit|[int](/API_docs/types/int.html) | Optional|


### Return type: [payments.SavedStarGifts](/API_docs/types/payments.SavedStarGifts.html)

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

$payments_SavedStarGifts = $MadelineProto->payments->getSavedStarGifts(exclude_unsaved: $Bool, exclude_saved: $Bool, exclude_unlimited: $Bool, exclude_limited: $Bool, exclude_unique: $Bool, sort_by_value: $Bool, peer: $InputPeer, offset: 'string', limit: $int, );
```

