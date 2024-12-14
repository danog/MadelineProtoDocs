---
title: "messages.getMyStickers"
description: "messages.getMyStickers parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getMyStickers.html
---
# Method: messages.getMyStickers
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|offset\_id|[long](/API_docs/types/long.html) | Yes|
|limit|[int](/API_docs/types/int.html) | Optional|


### Return type: [messages.MyStickers](/API_docs/types/messages.MyStickers.html)

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

$messages_MyStickers = $MadelineProto->messages->getMyStickers(offset_id: $long, limit: $int, );
```

