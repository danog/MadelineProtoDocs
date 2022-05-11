---
title: "messages.hidePeerSettingsBar"
description: "Should be called after the user hides the report spam/add as contact bar of a new chat, effectively prevents the user from executing the actions specified in the [peer's settings](../constructors/peerSettings.html)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_hidePeerSettingsBar.html
---
# Method: messages.hidePeerSettingsBar
[Back to methods index](index.html)



Should be called after the user hides the report spam/add as contact bar of a new chat, effectively prevents the user from executing the actions specified in the [peer's settings](../constructors/peerSettings.html).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

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
$Bool = $MadelineProto->messages->hidePeerSettingsBar(peer: InputPeer, );
```

