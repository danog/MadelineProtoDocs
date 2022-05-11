---
title: "channels.readMessageContents"
description: "Mark [channel/supergroup](https://core.telegram.org/api/channel) message contents as read"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_readMessageContents.html
---
# Method: channels.readMessageContents
[Back to methods index](index.html)



Mark [channel/supergroup](https://core.telegram.org/api/channel) message contents as read

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | [Channel/supergroup](https://core.telegram.org/api/channel) | Optional|
|id|Array of [int](/API_docs/types/int.html) | IDs of messages whose contents should be marked as read | Yes|


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
$Bool = $MadelineProto->channels->readMessageContents(channel: InputChannel, id: [int, int], );
```

