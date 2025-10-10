---
title: "stories.getAlbumStories"
description: "Get stories in a [story album »](https://core.telegram.org/api/stories#story-albums)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_getAlbumStories.html
---
# Method: stories.getAlbumStories
[Back to methods index](index.html)



Get stories in a [story album »](https://core.telegram.org/api/stories#story-albums).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where the album is posted. | Optional|
|album\_id|[int](/API_docs/types/int.html) | ID of the album. | Optional|
|offset|[int](/API_docs/types/int.html) | Offset for [pagination](https://core.telegram.org/api/offsets). | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|


### Return type: [stories.Stories](/API_docs/types/stories.Stories.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$stories_Stories = $MadelineProto->stories->getAlbumStories(peer: $InputPeer, album_id: $int, offset: $int, limit: $int, );
```

