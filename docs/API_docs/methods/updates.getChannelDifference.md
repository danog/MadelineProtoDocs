---
title: "updates.getChannelDifference"
description: "You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling updates"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/updates_getChannelDifference.html
---
# Method: updates.getChannelDifference
[Back to methods index](index.html)



You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling updates

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|force|[Bool](/API_docs/types/Bool.html) | Set to true to skip some possibly unneeded updates and reduce server-side load | Optional|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | The channel | Optional|
|filter|[ChannelMessagesFilter](/API_docs/types/ChannelMessagesFilter.html) | Messsage filter | Optional|
|pts|[int](/API_docs/types/int.html) | Persistent timestamp (see [updates](https://core.telegram.org/api/updates)) | Yes|
|limit|[int](/API_docs/types/int.html) | How many updates to fetch, max `100000`<br>Ordinary (non-bot) users are supposed to pass `10-100` | Yes|


### Return type: [updates.ChannelDifference](/API_docs/types/updates.ChannelDifference.html)

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
$updates_ChannelDifference = $MadelineProto->updates->getChannelDifference(force: Bool, channel: InputChannel, filter: ChannelMessagesFilter, pts: int, limit: int, );
```

