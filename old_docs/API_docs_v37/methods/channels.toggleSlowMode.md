---
title: channels.toggleSlowMode
description: Toggle supergroup slow mode: if enabled, users will only be able to send one message every `seconds` seconds
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_toggleSlowMode.html
---
# Method: channels.toggleSlowMode
[Back to methods index](index.md)



Toggle supergroup slow mode: if enabled, users will only be able to send one message every `seconds` seconds

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The [supergroup](https://core.telegram.org/api/channel) | Optional|
|seconds|[int](../types/int.md) | Users will only be able to send one message every `seconds` seconds, `0` to disable the limitation | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->channels->toggleSlowMode(['channel' => InputChannel, 'seconds' => int, ]);
```

Or, if you're into Lua:

```lua
Updates = channels.toggleSlowMode({channel=InputChannel, seconds=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHAT_NOT_MODIFIED|The pinned message wasn't modified|
|400|INPUT_METHOD_INVALID_1192227_X|Invalid method|
|400|INPUT_METHOD_INVALID_1604042050_X|Invalid method|
|400|SECONDS_INVALID|Invalid duration provided|


