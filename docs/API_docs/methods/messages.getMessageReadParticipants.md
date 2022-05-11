---
title: "messages.getMessageReadParticipants"
description: "Get which users read a specific message: only available for groups and supergroups with less than `chat_read_mark_size_threshold` members, read receipts will be stored for `chat_read_mark_expire_period` seconds after the message was sent, see [client configuration for more info »](https://core.telegram.org/api/config#client-configuration)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getMessageReadParticipants.html
---
# Method: messages.getMessageReadParticipants
[Back to methods index](index.html)



Get which users read a specific message: only available for groups and supergroups with less than `chat_read_mark_size_threshold` members, read receipts will be stored for `chat_read_mark_expire_period` seconds after the message was sent, see [client configuration for more info »](https://core.telegram.org/api/config#client-configuration).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Dialog | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Message ID | Yes|


### Return type: [Vector\_of\_long](/API_docs/types/long.html)

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
$Vector_of_long = $MadelineProto->messages->getMessageReadParticipants(peer: InputPeer, msg_id: int, );
```

