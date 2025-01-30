---
title: "payments.getConnectedStarRefBots"
description: "Fetch all affiliations we have created for a certain peer"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getConnectedStarRefBots.html
---
# Method: payments.getConnectedStarRefBots
[Back to methods index](index.html)



Fetch all affiliations we have created for a certain peer

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The affiliated peer | Optional|
|offset\_date|[int](/API_docs/types/int.html) | If set, returns only results older than the specified unixtime | Optional|
|offset\_link|[string](/API_docs/types/string.html) | Offset for [pagination](https://core.telegram.org/api/offsets), taken from the last returned [connectedBotStarRef](../constructors/connectedBotStarRef.html).`url` (initially empty) | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|


### Return type: [payments.ConnectedStarRefBots](/API_docs/types/payments.ConnectedStarRefBots.html)

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

$payments_ConnectedStarRefBots = $MadelineProto->payments->getConnectedStarRefBots(peer: $InputPeer, offset_date: $int, offset_link: 'string', limit: $int, );
```

