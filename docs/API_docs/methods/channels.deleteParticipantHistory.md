---
title: "channels.deleteParticipantHistory"
description: "channels.deleteParticipantHistory parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_deleteParticipantHistory.html
---
# Method: channels.deleteParticipantHistory
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.md) | Optional|
|participant|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.md) | Optional|


### Return type: [messages.AffectedHistory](/API_docs/types/messages.AffectedHistory.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_AffectedHistory = $MadelineProto->channels->deleteParticipantHistory(['channel' => InputChannel, 'participant' => InputPeer, ]);
```

