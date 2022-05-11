---
title: "channels.getSponsoredMessages"
description: "Get a list of sponsored messages"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getSponsoredMessages.html
---
# Method: channels.getSponsoredMessages
[Back to methods index](index.html)



Get a list of sponsored messages

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Peer | Optional|


### Return type: [messages.SponsoredMessages](/API_docs/types/messages.SponsoredMessages.html)

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
$messages_SponsoredMessages = $MadelineProto->channels->getSponsoredMessages(channel: InputChannel, );
```

