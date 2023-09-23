---
title: "stories.togglePinned"
description: "stories.togglePinned parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_togglePinned.html
---
# Method: stories.togglePinned
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|id|Array of [int](/API_docs/types/int.html) | Yes|
|pinned|[Bool](/API_docs/types/Bool.html) | Yes|


### Return type: [Vector\_of\_int](/API_docs/types/int.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_int = $MadelineProto->stories->togglePinned(peer: $InputPeer, id: [$int, $int], pinned: $Bool, );
```

