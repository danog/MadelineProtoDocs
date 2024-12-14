---
title: "messages.togglePeerTranslations"
description: "Show or hide the [real-time chat translation popup](https://core.telegram.org/api/translation) for a certain chat"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_togglePeerTranslations.html
---
# Method: messages.togglePeerTranslations
[Back to methods index](index.html)



Show or hide the [real-time chat translation popup](https://core.telegram.org/api/translation) for a certain chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|disabled|[Bool](/API_docs/types/Bool.html) | Whether to disable or enable the real-time chat translation popup | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->togglePeerTranslations(disabled: $Bool, peer: $InputPeer, );
```

