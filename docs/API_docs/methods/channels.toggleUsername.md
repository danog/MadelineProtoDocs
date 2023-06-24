---
title: "channels.toggleUsername"
description: "Activate or deactivate a purchased [fragment.com](https://fragment.com) username associated to a [supergroup or channel](https://core.telegram.org/api/channel) we own."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_toggleUsername.html
---
# Method: channels.toggleUsername
[Back to methods index](index.html)



Activate or deactivate a purchased [fragment.com](https://fragment.com) username associated to a [supergroup or channel](https://core.telegram.org/api/channel) we own.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | [Supergroup or channel](https://core.telegram.org/api/channel) | Optional|
|username|[string](/API_docs/types/string.html) | Username | Yes|
|active|[Bool](/API_docs/types/Bool.html) | Whether to activate or deactivate the username | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->channels->toggleUsername(channel: $InputChannel, username: 'string', active: $Bool, );
```

