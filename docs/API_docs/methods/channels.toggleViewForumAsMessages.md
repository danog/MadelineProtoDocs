---
title: "channels.toggleViewForumAsMessages"
description: "Users may also choose to display messages from all topics of a [forum](https://core.telegram.org/api/forum) as if they were sent to a normal group, using a 'View as messages' setting in the local client: this setting only affects the current account, and is synced to other logged in sessions using this method."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_toggleViewForumAsMessages.html
---
# Method: channels.toggleViewForumAsMessages
[Back to methods index](index.html)



Users may also choose to display messages from all topics of a [forum](https://core.telegram.org/api/forum) as if they were sent to a normal group, using a "View as messages" setting in the local client: this setting only affects the current account, and is synced to other logged in sessions using this method.

Invoking this method will update the value of the `view_forum_as_messages` flag of [channelFull](../constructors/channelFull.html) or [dialog](../constructors/dialog.html) and emit an [updateChannelViewForumAsMessages](../constructors/updateChannelViewForumAsMessages.html).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | The forum | Optional|
|enabled|[Bool](/API_docs/types/Bool.html) | The new value of the `view_forum_as_messages` flag. | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->channels->toggleViewForumAsMessages(channel: $InputChannel, enabled: $Bool, );
```

