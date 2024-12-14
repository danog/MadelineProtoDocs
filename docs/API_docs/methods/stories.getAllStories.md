---
title: "stories.getAllStories"
description: "Fetch the List of active (or active and hidden) stories, see [here »](https://core.telegram.org/api/stories#watching-stories) for more info on watching stories."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_getAllStories.html
---
# Method: stories.getAllStories
[Back to methods index](index.html)



Fetch the List of active (or active and hidden) stories, see [here »](https://core.telegram.org/api/stories#watching-stories) for more info on watching stories.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|next|[Bool](/API_docs/types/Bool.html) | If `next` and `state` are both set, uses the passed `state` to paginate to the next results; if neither `state` nor `next` are set, fetches the initial page; if `state` is set and `next` is not set, check for changes in the active/hidden peerset, see [here »](https://core.telegram.org/api/stories#watching-stories) for more info on the full flow. | Optional|
|hidden|[Bool](/API_docs/types/Bool.html) | If set, fetches the hidden active story list, otherwise fetches the active story list, see [here »](https://core.telegram.org/api/stories#watching-stories) for more info on the full flow. | Optional|
|state|[string](/API_docs/types/string.html) | If `next` and `state` are both set, uses the passed `state` to paginate to the next results; if neither `state` nor `next` are set, fetches the initial page; if `state` is set and `next` is not set, check for changes in the active/hidden peerset, see [here »](https://core.telegram.org/api/stories#watching-stories) for more info on the full flow. | Optional|


### Return type: [stories.AllStories](/API_docs/types/stories.AllStories.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$stories_AllStories = $MadelineProto->stories->getAllStories(next: $Bool, hidden: $Bool, state: 'string', );
```

