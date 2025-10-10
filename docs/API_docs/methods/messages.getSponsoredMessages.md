---
title: "messages.getSponsoredMessages"
description: "Get a list of [sponsored messages for a peer, see here »](https://core.telegram.org/api/sponsored-messages) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getSponsoredMessages.html
---
# Method: messages.getSponsoredMessages
[Back to methods index](index.html)



Get a list of [sponsored messages for a peer, see here »](https://core.telegram.org/api/sponsored-messages) for more info.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The currently open channel/bot. | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Must be set when fetching [sponsored messages to show on channel videos »](https://core.telegram.org/api/sponsored-messages#getting-sponsored-video-advertisements). | Optional|


### Return type: [messages.SponsoredMessages](/API_docs/types/messages.SponsoredMessages.html)

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

$messages_SponsoredMessages = $MadelineProto->messages->getSponsoredMessages(peer: $InputPeer, msg_id: $int, );
```

