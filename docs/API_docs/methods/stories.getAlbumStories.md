---
title: "stories.getAlbumStories"
description: "stories.getAlbumStories parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_getAlbumStories.html
---
# Method: stories.getAlbumStories
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|album\_id|[int](/API_docs/types/int.html) | Optional|
|offset|[int](/API_docs/types/int.html) | Optional|
|limit|[int](/API_docs/types/int.html) | Optional|


### Return type: [stories.Stories](/API_docs/types/stories.Stories.html)

### Can userbots use this method: **YES**

### Can bots use this method: **YES**


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

