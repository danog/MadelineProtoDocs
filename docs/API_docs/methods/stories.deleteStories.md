---
title: "stories.deleteStories"
description: "Deletes some posted [stories](https://core.telegram.org/api/stories)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_deleteStories.html
---
# Method: stories.deleteStories
[Back to methods index](index.html)



Deletes some posted [stories](https://core.telegram.org/api/stories).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Channel/user from where to delete stories. | Optional|
|id|Array of [int](/API_docs/types/int.html) | IDs of stories to delete. | Yes|


### Return type: [Vector\_of\_int](/API_docs/types/int.html)

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

$Vector_of_int = $MadelineProto->stories->deleteStories(peer: $InputPeer, id: [$int, $int], );
```

