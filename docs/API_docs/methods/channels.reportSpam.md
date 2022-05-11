---
title: "channels.reportSpam"
description: "Reports some messages from a user in a supergroup as spam; requires administrator rights in the supergroup"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_reportSpam.html
---
# Method: channels.reportSpam
[Back to methods index](index.html)



Reports some messages from a user in a supergroup as spam; requires administrator rights in the supergroup

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Supergroup | Optional|
|participant|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Participant whose messages should be reported | Optional|
|id|Array of [int](/API_docs/types/int.html) | IDs of spam messages | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Bool = $MadelineProto->channels->reportSpam(channel: InputChannel, participant: InputPeer, id: [int, int], );
```

