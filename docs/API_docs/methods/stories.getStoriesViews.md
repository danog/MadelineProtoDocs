---
title: "stories.getStoriesViews"
description: "Obtain info about the view count, forward count, reactions and recent viewers of one or more [stories](https://core.telegram.org/api/stories)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_getStoriesViews.html
---
# Method: stories.getStoriesViews
[Back to methods index](index.html)



Obtain info about the view count, forward count, reactions and recent viewers of one or more [stories](https://core.telegram.org/api/stories).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer whose stories should be fetched | Optional|
|id|Array of [int](/API_docs/types/int.html) | Story IDs | Yes|


### Return type: [stories.StoryViews](/API_docs/types/stories.StoryViews.html)

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

$stories_StoryViews = $MadelineProto->stories->getStoriesViews(peer: $InputPeer, id: [$int, $int], );
```

