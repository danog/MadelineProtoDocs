---
title: "channels.getForumTopics"
description: "channels.getForumTopics parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getForumTopics.html
---
# Method: channels.getForumTopics
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Optional|
|q|[string](/API_docs/types/string.html) | Optional|
|offset\_date|[int](/API_docs/types/int.html) | Yes|
|offset\_id|[int](/API_docs/types/int.html) | Yes|
|offset\_topic|[int](/API_docs/types/int.html) | Yes|
|limit|[int](/API_docs/types/int.html) | Yes|


### Return type: [messages.ForumTopics](/API_docs/types/messages.ForumTopics.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_ForumTopics = $MadelineProto->channels->getForumTopics(channel: InputChannel, q: 'string', offset_date: int, offset_id: int, offset_topic: int, limit: int, );
```

