---
title: channels.editAbout
description: channels.editAbout parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_editAbout.html
---
# Method: channels.editAbout
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Optional|
|about|[string](../types/string.md) | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->channels->editAbout(['channel' => InputChannel, 'about' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = channels.editAbout({channel=InputChannel, about='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHAT_ABOUT_NOT_MODIFIED|About text has not changed|
|400|CHAT_ABOUT_TOO_LONG|Chat about too long|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|


