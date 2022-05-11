---
title: "messages.uploadMedia"
description: "Upload a file and associate it to a chat (without actually sending it to the chat)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_uploadMedia.html
---
# Method: messages.uploadMedia
[Back to methods index](index.html)



Upload a file and associate it to a chat (without actually sending it to the chat)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The chat, can be an [inputPeerEmpty](../constructors/inputPeerEmpty.html) for bots | Optional|
|media|[MessageMedia, Update, Message or InputMedia](/API_docs/types/InputMedia.html) | File uploaded in chunks as described in [files »](https://core.telegram.org/api/files) | Optional|


### Return type: [MessageMedia](/API_docs/types/MessageMedia.html)

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
$MessageMedia = $MadelineProto->messages->uploadMedia(peer: InputPeer, media: InputMedia, );
```

