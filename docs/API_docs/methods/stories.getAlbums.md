---
title: "stories.getAlbums"
description: "Get [story albums](https://core.telegram.org/api/stories#story-albums) created by a peer."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_getAlbums.html
---
# Method: stories.getAlbums
[Back to methods index](index.html)



Get [story albums](https://core.telegram.org/api/stories#story-albums) created by a peer.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer. | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | The `hash` from a previously returned [stories.albums](../constructors/stories.albums.html), to avoid returning any results if they haven't changed. | Optional|


### Return type: [stories.Albums](/API_docs/types/stories.Albums.html)

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

$stories_Albums = $MadelineProto->stories->getAlbums(peer: $InputPeer, hash: [$long\|string, $long\|string], );
```

