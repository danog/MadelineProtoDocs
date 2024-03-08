---
title: "channels.getChannelRecommendations"
description: "Obtain a list of similarly themed public channels, selected based on similarities in their **subscriber bases**."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getChannelRecommendations.html
---
# Method: channels.getChannelRecommendations
[Back to methods index](index.html)



Obtain a list of similarly themed public channels, selected based on similarities in their **subscriber bases**.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | The method will return channels related to the passed `channel`. | Optional|


### Return type: [messages.Chats](/API_docs/types/messages.Chats.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Chats = $MadelineProto->channels->getChannelRecommendations(channel: $InputChannel, );
```

