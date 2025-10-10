---
title: "channels.updatePaidMessagesPrice"
description: "Enable or disable [paid messages »](https://core.telegram.org/api/paid-messages) in this [supergroup](https://core.telegram.org/api/channel) or [monoforum](https://core.telegram.org/api/monoforum)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_updatePaidMessagesPrice.html
---
# Method: channels.updatePaidMessagesPrice
[Back to methods index](index.html)



Enable or disable [paid messages »](https://core.telegram.org/api/paid-messages) in this [supergroup](https://core.telegram.org/api/channel) or [monoforum](https://core.telegram.org/api/monoforum).

Also used to [enable or disable monoforums aka direct messages in a channel](https://core.telegram.org/api/monoforum).

Note that passing the ID of the monoforum itself to `channel` will return a `CHANNEL_MONOFORUM_UNSUPPORTED` error: pass the ID of the associated channel to edit the settings of the associated monoforum, instead.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|broadcast\_messages\_allowed|[Bool](/API_docs/types/Bool.html) | Only usable for channels, enables or disables the associated [monoforum aka direct messages](https://core.telegram.org/api/monoforum). | Optional|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Pass the supergroup ID for supergroups and the ID of the [channel](https://core.telegram.org/api/channel) to modify the setting in the associated monoforum. | Optional|
|send\_paid\_messages\_stars|[long](/API_docs/types/long.html) | Specifies the required amount of [Telegram Stars](https://core.telegram.org/api/stars) users must pay to send messages to the supergroup or monoforum. | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->channels->updatePaidMessagesPrice(broadcast_messages_allowed: $Bool, channel: $InputChannel, send_paid_messages_stars: $long, );
```

