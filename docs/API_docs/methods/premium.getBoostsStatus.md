---
title: "premium.getBoostsStatus"
description: "Gets the current [number of boosts](https://core.telegram.org/api/boost) of a channel/supergroup."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/premium_getBoostsStatus.html
---
# Method: premium.getBoostsStatus
[Back to methods index](index.html)



Gets the current [number of boosts](https://core.telegram.org/api/boost) of a channel/supergroup.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer. | Optional|


### Return type: [premium.BoostsStatus](/API_docs/types/premium.BoostsStatus.html)

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

$premium_BoostsStatus = $MadelineProto->premium->getBoostsStatus(peer: $InputPeer, );
```

