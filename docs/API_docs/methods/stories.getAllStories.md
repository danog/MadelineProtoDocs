---
title: "stories.getAllStories"
description: "stories.getAllStories parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_getAllStories.html
---
# Method: stories.getAllStories
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|next|[Bool](/API_docs/types/Bool.html) | Optional|
|hidden|[Bool](/API_docs/types/Bool.html) | Optional|
|state|[string](/API_docs/types/string.html) | Optional|


### Return type: [stories.AllStories](/API_docs/types/stories.AllStories.html)

### Can bots use this method: **YES**


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

