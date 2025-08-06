---
title: "channels.toggleJoinToSend"
description: "Set whether all users [should join a discussion group in order to comment on a post »](https://core.telegram.org/api/discussion#requiring-users-to-join-the-group)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_toggleJoinToSend.html
---
# Method: channels.toggleJoinToSend
[Back to methods index](index.html)



Set whether all users [should join a discussion group in order to comment on a post »](https://core.telegram.org/api/discussion#requiring-users-to-join-the-group)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Discussion group | Optional|
|enabled|[Bool](/API_docs/types/Bool.html) | Toggle | Yes|


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

$Updates = $MadelineProto->channels->toggleJoinToSend(channel: $InputChannel, enabled: $Bool, );
```

