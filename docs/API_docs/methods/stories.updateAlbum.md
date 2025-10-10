---
title: "stories.updateAlbum"
description: "Rename a [story albums »](https://core.telegram.org/api/stories#story-albums), or add, delete or reorder stories in it."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_updateAlbum.html
---
# Method: stories.updateAlbum
[Back to methods index](index.html)



Rename a [story albums »](https://core.telegram.org/api/stories#story-albums), or add, delete or reorder stories in it.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where the album is posted. | Optional|
|album\_id|[int](/API_docs/types/int.html) | Album ID. | Optional|
|title|[string](/API_docs/types/string.html) | New album title. | Optional|
|delete\_stories|Array of [int](/API_docs/types/int.html) | If set, deletes the specified stories from the album. | Optional|
|add\_stories|Array of [int](/API_docs/types/int.html) | If set, adds the specified stories to the album. | Optional|
|order|Array of [int](/API_docs/types/int.html) | If set, reorders the stories in the album by their IDs. | Optional|


### Return type: [StoryAlbum](/API_docs/types/StoryAlbum.html)

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

$StoryAlbum = $MadelineProto->stories->updateAlbum(peer: $InputPeer, album_id: $int, title: 'string', delete_stories: [$int, $int], add_stories: [$int, $int], order: [$int, $int], );
```

