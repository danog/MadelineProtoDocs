---
title: "stories.getBoostersList"
description: "stories.getBoostersList parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_getBoostersList.html
---
# Method: stories.getBoostersList
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|offset|[string](/API_docs/types/string.html) | Yes|
|limit|[int](/API_docs/types/int.html) | Yes|


### Return type: [stories.BoostersList](/API_docs/types/stories.BoostersList.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$stories_BoostersList = $MadelineProto->stories->getBoostersList(peer: $InputPeer, offset: 'string', limit: $int, );
```

