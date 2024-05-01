---
title: "stories.getPeerStories"
description: "Fetch the full active [story list](https://core.telegram.org/api/stories#watching-stories) of a specific peer."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_getPeerStories.html
---
# Method: stories.getPeerStories
[Back to methods index](index.html)



Fetch the full active [story list](https://core.telegram.org/api/stories#watching-stories) of a specific peer.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer whose stories should be fetched | Optional|


### Return type: [stories.PeerStories](/API_docs/types/stories.PeerStories.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$stories_PeerStories = $MadelineProto->stories->getPeerStories(peer: $InputPeer, );
```

