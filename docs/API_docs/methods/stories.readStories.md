---
title: "stories.readStories"
description: "Mark all stories up to a certain ID as read, for a given peer; will emit an [updateReadStories](../constructors/updateReadStories.html) update to all logged-in sessions."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_readStories.html
---
# Method: stories.readStories
[Back to methods index](index.html)



Mark all stories up to a certain ID as read, for a given peer; will emit an [updateReadStories](../constructors/updateReadStories.html) update to all logged-in sessions.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer whose stories should be marked as read. | Optional|
|max\_id|[int](/API_docs/types/int.html) | Mark all stories up to and including this ID as read | Optional|


### Return type: [Vector\_of\_int](/API_docs/types/int.html)

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

$Vector_of_int = $MadelineProto->stories->readStories(peer: $InputPeer, max_id: $int, );
```

