---
title: "updates.getChannelDifference"
description: "You cannot use this method directly, please use the [event handler](https://docs.madelineproto.xyz/docs/UPDATES.html), instead."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/updates_getChannelDifference.html
---
# Method: updates.getChannelDifference
[Back to methods index](index.html)



# Warning: this is a low-level, complex method that **must never** be used directly.
The [event handler](https://docs.madelineproto.xyz/docs/UPDATES.html) provides a high-level abstraction that **must** be used instead of this method to fetch updates.
If you want to fetch all users of a bot using a bot token, use [getDialogIds](https://docs.madelineproto.xyz/docs/DIALOGS.html) or the high-level [broadcast API](https://docs.madelineproto.xyz/docs/BROADCAST.html), instead.

You cannot use this method directly, please use the [event handler](https://docs.madelineproto.xyz/docs/UPDATES.html), instead.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|force|[Bool](/API_docs/types/Bool.html) | Set to true to skip some possibly unneeded updates and reduce server-side load | Optional|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | The channel | Optional|
|filter|[ChannelMessagesFilter](/API_docs/types/ChannelMessagesFilter.html) | Messsage filter | Optional|
|pts|[int](/API_docs/types/int.html) | Persistent timestamp (see [updates](https://core.telegram.org/api/updates)) | Optional|
|limit|[int](/API_docs/types/int.html) | How many updates to fetch, max `100000`<br>Ordinary (non-bot) users are supposed to pass `10-100` | Optional|


### Return type: [updates.ChannelDifference](/API_docs/types/updates.ChannelDifference.html)

### Can userbots use this method: **YES**

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$updates_ChannelDifference = $MadelineProto->updates->getChannelDifference(force: $Bool, channel: $InputChannel, filter: $ChannelMessagesFilter, pts: $int, limit: $int, );
```

