---
title: "stories.getStoryReactionsList"
description: "stories.getStoryReactionsList parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_getStoryReactionsList.html
---
# Method: stories.getStoryReactionsList
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|forwards\_first|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|id|[int](/API_docs/types/int.html) | Optional|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Optional|
|offset|[string](/API_docs/types/string.html) | Optional|
|limit|[int](/API_docs/types/int.html) | Optional|


### Return type: [stories.StoryReactionsList](/API_docs/types/stories.StoryReactionsList.html)

### Can bots use this method: **YES**


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

