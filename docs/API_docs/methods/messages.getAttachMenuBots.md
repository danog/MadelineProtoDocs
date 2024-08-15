---
title: "messages.getAttachMenuBots"
description: "Returns installed attachment menu [bot mini apps »](https://core.telegram.org/api/bots/attach)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getAttachMenuBots.html
---
# Method: messages.getAttachMenuBots
[Back to methods index](index.html)



Returns installed attachment menu [bot mini apps »](https://core.telegram.org/api/bots/attach)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [long|string](/API_docs/types/long|string.html) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [AttachMenuBots](/API_docs/types/AttachMenuBots.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$AttachMenuBots = $MadelineProto->messages->getAttachMenuBots(hash: [$long|string, $long|string], );
```

