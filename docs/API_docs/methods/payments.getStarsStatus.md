---
title: "payments.getStarsStatus"
description: "Get the current [Telegram Stars balance](https://core.telegram.org/api/stars) of the current account (with peer=[inputPeerSelf](../constructors/inputPeerSelf.html)), or the stars balance of the bot specified in `peer`."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getStarsStatus.html
---
# Method: payments.getStarsStatus
[Back to methods index](index.html)



Get the current [Telegram Stars balance](https://core.telegram.org/api/stars) of the current account (with peer=[inputPeerSelf](../constructors/inputPeerSelf.html)), or the stars balance of the bot specified in `peer`.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer of which to get the balance. | Optional|


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

$payments_StarsStatus = $MadelineProto->payments->getStarsStatus(peer: $InputPeer, );
```

