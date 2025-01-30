---
title: "channels.restrictSponsoredMessages"
description: "Disable ads on the specified channel, for all users."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_restrictSponsoredMessages.html
---
# Method: channels.restrictSponsoredMessages
[Back to methods index](index.html)



Disable ads on the specified channel, for all users.

Available only after reaching at least the [boost level »](https://core.telegram.org/api/boost) specified in the [`channel_restrict_sponsored_level_min` »](https://core.telegram.org/api/config#channel-restrict-sponsored-level-min) config parameter.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | The channel. | Optional|
|restricted|[Bool](/API_docs/types/Bool.html) | Whether to disable or re-enable ads. | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->channels->restrictSponsoredMessages(channel: $InputChannel, restricted: $Bool, );
```

