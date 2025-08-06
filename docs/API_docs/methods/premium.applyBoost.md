---
title: "premium.applyBoost"
description: "Apply one or more [boosts »](https://core.telegram.org/api/boost) to a peer."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/premium_applyBoost.html
---
# Method: premium.applyBoost
[Back to methods index](index.html)



Apply one or more [boosts »](https://core.telegram.org/api/boost) to a peer.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|slots|Array of [int](/API_docs/types/int.html) | Which [boost slots](https://core.telegram.org/api/boost) to assign to this peer. | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer to boost. | Optional|


### Return type: [premium.MyBoosts](/API_docs/types/premium.MyBoosts.html)

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

$premium_MyBoosts = $MadelineProto->premium->applyBoost(slots: [$int, $int], peer: $InputPeer, );
```

