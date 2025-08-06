---
title: "premium.getBoostsList"
description: "Obtains info about the boosts that were applied to a certain channel or supergroup (admins only)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/premium_getBoostsList.html
---
# Method: premium.getBoostsList
[Back to methods index](index.html)



Obtains info about the boosts that were applied to a certain channel or supergroup (admins only)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|gifts|[Bool](/API_docs/types/Bool.html) | Whether to return only info about boosts received from [gift codes and giveaways created by the channel/supergroup »](https://core.telegram.org/api/giveaways) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The channel/supergroup | Optional|
|offset|[string](/API_docs/types/string.html) | Offset for pagination, obtained from [premium.boostsList](../constructors/premium.boostsList.html).`next_offset` | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|


### Return type: [premium.BoostsList](/API_docs/types/premium.BoostsList.html)

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

$premium_BoostsList = $MadelineProto->premium->getBoostsList(gifts: $Bool, peer: $InputPeer, offset: 'string', limit: $int, );
```

