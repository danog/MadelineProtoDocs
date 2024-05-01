---
title: "stories.toggleAllStoriesHidden"
description: "Hide the active stories of a specific peer, preventing them from being displayed on the action bar on the homescreen."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_toggleAllStoriesHidden.html
---
# Method: stories.toggleAllStoriesHidden
[Back to methods index](index.html)



Hide the active stories of a specific peer, preventing them from being displayed on the action bar on the homescreen.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hidden|[Bool](/API_docs/types/Bool.html) | Whether to hide or unhide all active stories of the peer | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->stories->toggleAllStoriesHidden(hidden: $Bool, );
```

