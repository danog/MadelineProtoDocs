---
title: "channels.getParticipant"
description: "Get info about a [channel/supergroup](https://core.telegram.org/api/channel) participant"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getParticipant.html
---
# Method: channels.getParticipant
[Back to methods index](index.html)



Get info about a [channel/supergroup](https://core.telegram.org/api/channel) participant

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Channel/supergroup | Optional|
|participant|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Participant to get info about | Optional|


### Return type: [channels.ChannelParticipant](/API_docs/types/channels.ChannelParticipant.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$channels_ChannelParticipant = $MadelineProto->channels->getParticipant(channel: InputChannel, participant: InputPeer, );
```

