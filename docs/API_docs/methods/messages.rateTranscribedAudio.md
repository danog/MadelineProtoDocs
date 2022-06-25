---
title: "messages.rateTranscribedAudio"
description: "messages.rateTranscribedAudio parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_rateTranscribedAudio.html
---
# Method: messages.rateTranscribedAudio
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Yes|
|transcription\_id|[long](/API_docs/types/long.html) | Yes|
|good|[Bool](/API_docs/types/Bool.html) | Yes|


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
$Bool = $MadelineProto->messages->rateTranscribedAudio(peer: InputPeer, msg_id: int, transcription_id: long, good: Bool, );
```

