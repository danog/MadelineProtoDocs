---
title: "stories.getPinnedStories"
description: "Fetch the [stories](https://core.telegram.org/api/stories#pinned-or-archived-stories) pinned on a peer's profile."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_getPinnedStories.html
---
# Method: stories.getPinnedStories
[Back to methods index](index.html)



Fetch the [stories](https://core.telegram.org/api/stories#pinned-or-archived-stories) pinned on a peer's profile.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer whose pinned stories should be fetched | Optional|
|offset\_id|[int](/API_docs/types/int.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|


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

$stories_Stories = $MadelineProto->stories->getPinnedStories(peer: $InputPeer, offset_id: $int, limit: $int, );
```

