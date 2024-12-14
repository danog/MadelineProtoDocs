---
title: "channels.getForumTopics"
description: "Get [topics of a forum](https://core.telegram.org/api/forum)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getForumTopics.html
---
# Method: channels.getForumTopics
[Back to methods index](index.html)



Get [topics of a forum](https://core.telegram.org/api/forum)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Supergroup | Optional|
|q|[string](/API_docs/types/string.html) | Search query | Optional|
|offset\_date|[int](/API_docs/types/int.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets), date of the last message of the last found topic. Use 0 or any date in the future to get results from the last topic. | Optional|
|offset\_id|[int](/API_docs/types/int.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets), ID of the last message of the last found topic (or initially `0`). | Optional|
|offset\_topic|[int](/API_docs/types/int.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets), ID of the last found topic (or initially `0`). | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets). For optimal performance, the number of returned topics is chosen by the server and can be smaller than the specified limit. | Optional|


### Return type: [messages.ForumTopics](/API_docs/types/messages.ForumTopics.html)

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

$messages_ForumTopics = $MadelineProto->channels->getForumTopics(channel: $InputChannel, q: 'string', offset_date: $int, offset_id: $int, offset_topic: $int, limit: $int, );
```

