---
title: "channels.toggleSlowMode"
description: "Toggle supergroup slow mode: if enabled, users will only be able to send one message every `seconds` seconds"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_toggleSlowMode.html
---
# Method: channels.toggleSlowMode
[Back to methods index](index.html)



Toggle supergroup slow mode: if enabled, users will only be able to send one message every `seconds` seconds

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | The [supergroup](https://core.telegram.org/api/channel) | Optional|
|seconds|[int](/API_docs/types/int.html) | Users will only be able to send one message every `seconds` seconds, `0` to disable the limitation | Yes|


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

// PHP 8+ syntax, use an array on PHP 7.
$Updates = $MadelineProto->channels->toggleSlowMode(channel: InputChannel, seconds: int, );
```

