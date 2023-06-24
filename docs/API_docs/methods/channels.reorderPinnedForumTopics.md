---
title: "channels.reorderPinnedForumTopics"
description: "Reorder pinned forum topics"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_reorderPinnedForumTopics.html
---
# Method: channels.reorderPinnedForumTopics
[Back to methods index](index.html)



Reorder pinned forum topics

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|force|[Bool](/API_docs/types/Bool.html) | If set, topics pinned server-side but not present in the order field will be unpinned. | Optional|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Supergroup ID | Optional|
|order|Array of [int](/API_docs/types/int.html) | [Topic IDs »](https://core.telegram.org/api/forum) | Yes|


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

$Updates = $MadelineProto->channels->reorderPinnedForumTopics(force: $Bool, channel: $InputChannel, order: [$int, $int], );
```

