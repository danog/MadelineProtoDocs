---
title: "stories.getStoriesByID"
description: "Obtain full info about a set of [stories](https://core.telegram.org/api/stories) by their IDs."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_getStoriesByID.html
---
# Method: stories.getStoriesByID
[Back to methods index](index.html)



Obtain full info about a set of [stories](https://core.telegram.org/api/stories) by their IDs.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where the stories were posted | Optional|
|id|Array of [int](/API_docs/types/int.html) | Story IDs | Yes|


### Return type: [stories.Stories](/API_docs/types/stories.Stories.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$stories_Stories = $MadelineProto->stories->getStoriesByID(peer: $InputPeer, id: [$int, $int], );
```

