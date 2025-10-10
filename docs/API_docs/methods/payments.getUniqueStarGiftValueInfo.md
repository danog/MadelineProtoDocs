---
title: "payments.getUniqueStarGiftValueInfo"
description: "Get information about the value of a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getUniqueStarGiftValueInfo.html
---
# Method: payments.getUniqueStarGiftValueInfo
[Back to methods index](index.html)



Get information about the value of a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|slug|[string](/API_docs/types/string.html) | `slug` from a [starGiftUnique](../constructors/starGiftUnique.html). | Optional|


### Return type: [payments.UniqueStarGiftValueInfo](/API_docs/types/payments.UniqueStarGiftValueInfo.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments_UniqueStarGiftValueInfo = $MadelineProto->payments->getUniqueStarGiftValueInfo(slug: 'string', );
```

