---
title: "channels.toggleSignatures"
description: "Enable/disable message signatures in channels"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_toggleSignatures.html
---
# Method: channels.toggleSignatures
[Back to methods index](index.html)



Enable/disable message signatures in channels

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|signatures\_enabled|[Bool](/API_docs/types/Bool.html) | If set, enables message signatures. | Optional|
|profiles\_enabled|[Bool](/API_docs/types/Bool.html) | If set, messages from channel admins will link to their profiles, just like for group messages: can only be set if the `signatures_enabled` flag is set. | Optional|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Channel | Optional|


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

$Updates = $MadelineProto->channels->toggleSignatures(signatures_enabled: $Bool, profiles_enabled: $Bool, channel: $InputChannel, );
```

