---
title: "stories.getStoryViewsList"
description: "stories.getStoryViewsList parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_getStoryViewsList.html
---
# Method: stories.getStoryViewsList
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[int](/API_docs/types/int.html) | Yes|
|offset\_date|[int](/API_docs/types/int.html) | Yes|
|offset\_id|[long](/API_docs/types/long.html) | Yes|
|limit|[int](/API_docs/types/int.html) | Yes|


### Return type: [stories.StoryViewsList](/API_docs/types/stories.StoryViewsList.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$stories_StoryViewsList = $MadelineProto->stories->getStoryViewsList(id: $int, offset_date: $int, offset_id: $long, limit: $int, );
```

