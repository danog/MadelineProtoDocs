---
title: "messages.setTyping"
description: "Sends a current user typing event (see [SendMessageAction](../types/SendMessageAction.html) for all event types) to a conversation partner or group."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setTyping.html
---
# Method: messages.setTyping
[Back to methods index](index.html)



Sends a current user typing event (see [SendMessageAction](../types/SendMessageAction.html) for all event types) to a conversation partner or group.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Target user or group | Optional|
|top\_msg\_id|[int](/API_docs/types/int.html) | [Thread ID](https://core.telegram.org/api/threads) | Optional|
|action|[SendMessageAction](/API_docs/types/SendMessageAction.html) | Type of action<br>Parameter added in [Layer 17](https://core.telegram.org/api/layers#layer-17). | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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
$Bool = $MadelineProto->messages->setTyping(peer: InputPeer, top_msg_id: int, action: SendMessageAction, );
```

