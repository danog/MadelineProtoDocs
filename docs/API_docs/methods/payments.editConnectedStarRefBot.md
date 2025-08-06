---
title: "payments.editConnectedStarRefBot"
description: "Leave a bot's [affiliate program »](https://core.telegram.org/api/bots/referrals#becoming-an-affiliate)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_editConnectedStarRefBot.html
---
# Method: payments.editConnectedStarRefBot
[Back to methods index](index.html)



Leave a bot's [affiliate program »](https://core.telegram.org/api/bots/referrals#becoming-an-affiliate)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|revoked|[Bool](/API_docs/types/Bool.html) | If set, leaves the bot's affiliate program | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer that was affiliated | Optional|
|link|[string](/API_docs/types/string.html) | The affiliate link to revoke | Optional|


### Return type: [payments.ConnectedStarRefBots](/API_docs/types/payments.ConnectedStarRefBots.html)

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

$payments_ConnectedStarRefBots = $MadelineProto->payments->editConnectedStarRefBot(revoked: $Bool, peer: $InputPeer, link: 'string', );
```

