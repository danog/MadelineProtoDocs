---
title: "messages.getAttachMenuBots"
description: "messages.getAttachMenuBots parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getAttachMenuBots.html
---
# Method: messages.getAttachMenuBots
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[long](/API_docs/types/long.html) | Yes|


### Return type: [AttachMenuBots](/API_docs/types/AttachMenuBots.html)

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
$AttachMenuBots = $MadelineProto->messages->getAttachMenuBots(hash: long, );
```

