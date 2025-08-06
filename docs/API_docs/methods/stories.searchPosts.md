---
title: "stories.searchPosts"
description: "Globally search for [stories](https://core.telegram.org/api/stories) using a hashtag or a [location media area](https://core.telegram.org/api/stories#location-tags), see [here »](https://core.telegram.org/api/stories#searching-stories) for more info on the full flow."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_searchPosts.html
---
# Method: stories.searchPosts
[Back to methods index](index.html)



Globally search for [stories](https://core.telegram.org/api/stories) using a hashtag or a [location media area](https://core.telegram.org/api/stories#location-tags), see [here »](https://core.telegram.org/api/stories#searching-stories) for more info on the full flow.

Either `hashtag` **or** `area` **must** be set when invoking the method.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hashtag|[string](/API_docs/types/string.html) | Hashtag (without the `#`) | Optional|
|area|[MediaArea](/API_docs/types/MediaArea.html) | A [mediaAreaGeoPoint](../constructors/mediaAreaGeoPoint.html) or a [mediaAreaVenue](../constructors/mediaAreaVenue.html).  <br>Note [mediaAreaGeoPoint](../constructors/mediaAreaGeoPoint.html) areas may be searched only if they have an associated `address`. | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | If set, returns only stories posted by this peer. | Optional|
|offset|[string](/API_docs/types/string.html) | Offset for [pagination](https://core.telegram.org/api/offsets): initially an empty string, then the `next_offset` from the previously returned [stories.foundStories](../constructors/stories.foundStories.html). | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|


### Return type: [stories.FoundStories](/API_docs/types/stories.FoundStories.html)

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

$stories_FoundStories = $MadelineProto->stories->searchPosts(hashtag: 'string', area: $MediaArea, peer: $InputPeer, offset: 'string', limit: $int, );
```

