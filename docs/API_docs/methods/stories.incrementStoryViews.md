---
title: "stories.incrementStoryViews"
description: "Increment the view counter of one or more stories."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_incrementStoryViews.html
---
# Method: stories.incrementStoryViews
[Back to methods index](index.html)



Increment the view counter of one or more stories.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where the stories were posted. | Optional|
|id|Array of [int](/API_docs/types/int.html) | IDs of the stories (maximum 200 at a time). | Yes|


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

$Bool = $MadelineProto->stories->incrementStoryViews(peer: $InputPeer, id: [$int, $int], );
```

