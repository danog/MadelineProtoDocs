---
title: channels.createChannel
description: Create channel/supergroup
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.createChannel  
[Back to methods index](index.md)


Create channel/supergroup

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|broadcast|[Bool](../types/Bool.md) | Set this to true to create a channel | Optional|
|megagroup|[Bool](../types/Bool.md) | Set this to true to create a supergroup | Optional|
|title|[string](../types/string.md) | Supergroup/channel title | Yes|
|about|[string](../types/string.md) | About text | Yes|


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

$Updates = $MadelineProto->channels->createChannel(['broadcast' => Bool, 'megagroup' => Bool, 'title' => 'string', 'about' => 'string', ]);
```

Or, if you're into Lua:

```lua
Updates = channels.createChannel({broadcast=Bool, megagroup=Bool, title='string', about='string', })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHAT_TITLE_EMPTY|No chat title provided|
|USER_RESTRICTED|You're spamreported, you can't create channels or chats.|
|USER_RESTRICTED|You're spamreported, you can't create channels or chats.|


