---
title: "messages.transcribeAudio"
description: "[Transcribe voice message](https://core.telegram.org/api/transcribe)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_transcribeAudio.html
---
# Method: messages.transcribeAudio
[Back to methods index](index.html)



[Transcribe voice message](https://core.telegram.org/api/transcribe)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer ID where the voice message was sent | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Voice message ID | Optional|


### Return type: [messages.TranscribedAudio](/API_docs/types/messages.TranscribedAudio.html)

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
$messages_TranscribedAudio = $MadelineProto->messages->transcribeAudio(peer: InputPeer, msg_id: int, );
```

