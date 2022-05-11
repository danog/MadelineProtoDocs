---
title: "channels.getInactiveChannels"
description: "Get inactive channels and supergroups"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getInactiveChannels.html
---
# Method: channels.getInactiveChannels
[Back to methods index](index.html)



Get inactive channels and supergroups



### Return type: [messages.InactiveChats](/API_docs/types/messages.InactiveChats.html)

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
$messages_InactiveChats = $MadelineProto->channels->getInactiveChannels();
```

