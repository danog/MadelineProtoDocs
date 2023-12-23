---
title: "messages.sendBotRequestedPeer"
description: "Send a chosen peer, as requested by a [keyboardButtonRequestPeer](../constructors/keyboardButtonRequestPeer.html) button."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendBotRequestedPeer.html
---
# Method: messages.sendBotRequestedPeer
[Back to methods index](index.html)



Send a chosen peer, as requested by a [keyboardButtonRequestPeer](../constructors/keyboardButtonRequestPeer.html) button.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The bot that sent the [keyboardButtonRequestPeer](../constructors/keyboardButtonRequestPeer.html) button. | Optional|
|msg\_id|[int](/API_docs/types/int.html) | ID of the message that contained the reply keyboard with the [keyboardButtonRequestPeer](../constructors/keyboardButtonRequestPeer.html) button. | Optional|
|button\_id|[int](/API_docs/types/int.html) | The `button_id` field from the [keyboardButtonRequestPeer](../constructors/keyboardButtonRequestPeer.html) constructor. | Optional|
|requested\_peers|Array of [Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) |  | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->sendBotRequestedPeer(peer: $InputPeer, msg_id: $int, button_id: $int, requested_peers: [$InputPeer, $InputPeer], );
```

