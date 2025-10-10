---
title: "stories.createAlbum"
description: "Creates a [story album](https://core.telegram.org/api/stories#story-albums)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_createAlbum.html
---
# Method: stories.createAlbum
[Back to methods index](index.html)



Creates a [story album](https://core.telegram.org/api/stories#story-albums).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The owned peer where to create the album. | Optional|
|title|[string](/API_docs/types/string.html) | Album name. | Optional|
|stories|Array of [int](/API_docs/types/int.html) | Stories to add to the album. | Yes|


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

$StoryAlbum = $MadelineProto->stories->createAlbum(peer: $InputPeer, title: 'string', stories: [$int, $int], );
```

