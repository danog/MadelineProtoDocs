---
title: "payments.getGiveawayInfo"
description: "Obtain information about a [Telegram Premium giveaway »](https://core.telegram.org/api/giveaways)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getGiveawayInfo.html
---
# Method: payments.getGiveawayInfo
[Back to methods index](index.html)



Obtain information about a [Telegram Premium giveaway »](https://core.telegram.org/api/giveaways).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer where the giveaway was posted. | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Message ID of the [messageActionGiveawayLaunch](../constructors/messageActionGiveawayLaunch.html) service message | Optional|


### Return type: [payments.GiveawayInfo](/API_docs/types/payments.GiveawayInfo.html)

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

$payments_GiveawayInfo = $MadelineProto->payments->getGiveawayInfo(peer: $InputPeer, msg_id: $int, );
```

