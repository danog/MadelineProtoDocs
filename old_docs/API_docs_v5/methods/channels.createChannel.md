---
title: channels.createChannel
description: Create a [supergroup/channel](https://core.telegram.org/api/channel).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_createChannel.html
---
# Method: channels.createChannel
[Back to methods index](index.md)



Create a [supergroup/channel](https://core.telegram.org/api/channel).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|title|[string](../types/string.md) | Channel title | Yes|
|about|[string](../types/string.md) | Channel description | Yes|
|users|Array of [Username, chat ID, Update, Message or InputUser](../types/InputUser.md) |  | Yes|


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

$Updates = $MadelineProto->channels->createChannel(['title' => 'string', 'about' => 'string', 'users' => [InputUser, InputUser], ]);
```

Or, if you're into Lua:

```lua
Updates = channels.createChannel({title='string', about='string', users={InputUser}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNELS_TOO_MUCH|You have joined too many channels/supergroups|
|400|CHAT_ABOUT_TOO_LONG|Chat about too long|
|400|CHAT_TITLE_EMPTY|No chat title provided|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|406|USER_RESTRICTED|You're spamreported, you can't create channels or chats.|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|
|403|USER_RESTRICTED|You're spamreported, you can't create channels or chats.|


