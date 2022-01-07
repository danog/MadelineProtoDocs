---
title: "channels.checkUsername"
description: "Check if a username is free and can be assigned to a channel/supergroup"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_checkUsername.html
---
# Method: channels.checkUsername
[Back to methods index](index.html)



Check if a username is free and can be assigned to a channel/supergroup

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | The [channel/supergroup](https://core.telegram.org/api/channel) that will assigned the specified username | Optional|
|username|[string](/API_docs/types/string.html) | The username to check | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->channels->checkUsername(['channel' => InputChannel, 'username' => 'string', ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNELS_ADMIN_PUBLIC_TOO_MUCH|You're admin of too many public channels, make some channels private to change the username of this channel|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|USERNAME_INVALID|The provided username is not valid|


