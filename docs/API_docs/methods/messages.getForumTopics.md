---
title: "messages.getForumTopics"
description: "messages.getForumTopics parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getForumTopics.html
---
# Method: messages.getForumTopics
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|q|[string](/API_docs/types/string.html) | Optional|
|offset\_date|[int](/API_docs/types/int.html) | Optional|
|offset\_id|[int](/API_docs/types/int.html) | Optional|
|offset\_topic|[int](/API_docs/types/int.html) | Optional|
|limit|[int](/API_docs/types/int.html) | Optional|


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

$messages_ForumTopics = $MadelineProto->messages->getForumTopics(peer: $InputPeer, q: 'string', offset_date: $int, offset_id: $int, offset_topic: $int, limit: $int, );
```

