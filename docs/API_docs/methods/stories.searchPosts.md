---
title: "stories.searchPosts"
description: "stories.searchPosts parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_searchPosts.html
---
# Method: stories.searchPosts
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hashtag|[string](/API_docs/types/string.html) | Optional|
|area|[MediaArea](/API_docs/types/MediaArea.html) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|offset|[string](/API_docs/types/string.html) | Optional|
|limit|[int](/API_docs/types/int.html) | Optional|


### Return type: [stories.FoundStories](/API_docs/types/stories.FoundStories.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$stories_FoundStories = $MadelineProto->stories->searchPosts(hashtag: 'string', area: $MediaArea, peer: $InputPeer, offset: 'string', limit: $int, );
```

