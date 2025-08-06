---
title: "channels.getForumTopicsByID"
description: "Get forum topics by their ID"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getForumTopicsByID.html
---
# Method: channels.getForumTopicsByID
[Back to methods index](index.html)



Get forum topics by their ID

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Forum | Optional|
|topics|Array of [int](/API_docs/types/int.html) | Topic IDs | Yes|


### Return type: [messages.ForumTopics](/API_docs/types/messages.ForumTopics.html)

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

$messages_ForumTopics = $MadelineProto->channels->getForumTopicsByID(channel: $InputChannel, topics: [$int, $int], );
```

