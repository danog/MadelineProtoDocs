---
title: "stories.getStoryReactionsList"
description: "Get the [reaction](https://core.telegram.org/api/reactions) and interaction list of a [story](https://core.telegram.org/api/stories) posted to a channel, along with the sender of each reaction."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_getStoryReactionsList.html
---
# Method: stories.getStoryReactionsList
[Back to methods index](index.html)



Get the [reaction](https://core.telegram.org/api/reactions) and interaction list of a [story](https://core.telegram.org/api/stories) posted to a channel, along with the sender of each reaction.

Can only be used by channel admins.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|forwards\_first|[Bool](/API_docs/types/Bool.html) | If set, returns forwards and reposts first, then reactions, then other views; otherwise returns interactions sorted just by interaction date. | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Channel | Optional|
|id|[int](/API_docs/types/int.html) | [Story](https://core.telegram.org/api/stories) ID | Optional|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Get only reactions of this type | Optional|
|offset|[string](/API_docs/types/string.html) | Offset for pagination (taken from the `next_offset` field of the returned [stories.StoryReactionsList](../types/stories.StoryReactionsList.html)); empty in the first request. | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|


### Return type: [stories.StoryReactionsList](/API_docs/types/stories.StoryReactionsList.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$stories_StoryReactionsList = $MadelineProto->stories->getStoryReactionsList(forwards_first: $Bool, peer: $InputPeer, id: $int, reaction: $Reaction, offset: 'string', limit: $int, );
```

