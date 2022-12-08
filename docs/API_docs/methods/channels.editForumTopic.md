---
title: "channels.editForumTopic"
description: "channels.editForumTopic parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_editForumTopic.html
---
# Method: channels.editForumTopic
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Optional|
|topic\_id|[int](/API_docs/types/int.html) | Yes|
|title|[string](/API_docs/types/string.html) | Optional|
|icon\_emoji\_id|[long](/API_docs/types/long.html) | Optional|
|closed|[Bool](/API_docs/types/Bool.html) | Optional|
|hidden|[Bool](/API_docs/types/Bool.html) | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Updates = $MadelineProto->channels->editForumTopic(channel: InputChannel, topic_id: int, title: 'string', icon_emoji_id: long, closed: Bool, hidden: Bool, );
```

