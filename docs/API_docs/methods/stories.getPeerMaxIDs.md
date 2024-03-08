---
title: "stories.getPeerMaxIDs"
description: "Get the IDs of the maximum read stories for a set of peers."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_getPeerMaxIDs.html
---
# Method: stories.getPeerMaxIDs
[Back to methods index](index.html)



Get the IDs of the maximum read stories for a set of peers.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peers | Yes|


### Return type: [Vector\_of\_int](/API_docs/types/int.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_int = $MadelineProto->stories->getPeerMaxIDs(id: [$InputPeer, $InputPeer], );
```

