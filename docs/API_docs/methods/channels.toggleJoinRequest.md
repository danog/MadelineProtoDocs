---
title: "channels.toggleJoinRequest"
description: "Set whether all users should [request admin approval to join the group »](https://core.telegram.org/api/invites#join-requests)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_toggleJoinRequest.html
---
# Method: channels.toggleJoinRequest
[Back to methods index](index.html)



Set whether all users should [request admin approval to join the group »](https://core.telegram.org/api/invites#join-requests).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Group | Optional|
|enabled|[Bool](/API_docs/types/Bool.html) | Toggle | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->channels->toggleJoinRequest(channel: InputChannel, enabled: Bool, );
```

