---
title: "stats.getMessagePublicForwards"
description: "Obtains a list of messages, indicating to which other public channels was a channel message forwarded.  "
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stats_getMessagePublicForwards.html
---
# Method: stats.getMessagePublicForwards
[Back to methods index](index.html)



Obtains a list of messages, indicating to which other public channels was a channel message forwarded.  
Will return a list of [messages](../constructors/message.html) with `peer_id` equal to the public channel to which this message was forwarded.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Source channel | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Source message ID | Optional|
|offset|[string](/API_docs/types/string.html) | Offset for [pagination](https://core.telegram.org/api/offsets), empty string on first call, then use the `next_offset` field of the returned constructor (if present, otherwise no more results are available). | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|


### Return type: [stats.PublicForwards](/API_docs/types/stats.PublicForwards.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$stats_PublicForwards = $MadelineProto->stats->getMessagePublicForwards(channel: $InputChannel, msg_id: $int, offset: 'string', limit: $int, );
```

