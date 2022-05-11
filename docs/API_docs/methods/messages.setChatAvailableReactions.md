---
title: "messages.setChatAvailableReactions"
description: "Change the set of [message reactions »](https://core.telegram.org/api/reactions) that can be used in a certain group, supergroup or channel"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setChatAvailableReactions.html
---
# Method: messages.setChatAvailableReactions
[Back to methods index](index.html)



Change the set of [message reactions »](https://core.telegram.org/api/reactions) that can be used in a certain group, supergroup or channel

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Group where to apply changes | Optional|
|available\_reactions|Array of [string](/API_docs/types/string.html) | Allowed reaction emojis | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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
$Updates = $MadelineProto->messages->setChatAvailableReactions(peer: InputPeer, available_reactions: ['string', 'string'], );
```

