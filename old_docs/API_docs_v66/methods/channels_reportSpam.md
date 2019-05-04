---
title: channels.reportSpam
description: Report a message in a supergroup/channel for spam
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.reportSpam  
[Back to methods index](index.md)


Report a message in a supergroup/channel for spam

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The user that sent the messages | Optional|
|id|Array of [int](../types/int.md) | The IDs of messages to report | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->channels->reportSpam(['channel' => InputChannel, 'user_id' => InputUser, 'id' => [int, int], ]);
```

Or, if you're into Lua:

```lua
Bool = channels.reportSpam({channel=InputChannel, user_id=InputUser, id={int}, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHANNEL_INVALID|The provided channel is invalid|
|INPUT_USER_DEACTIVATED|The specified user was deleted|


