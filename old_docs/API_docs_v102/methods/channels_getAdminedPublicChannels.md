---
title: channels.getAdminedPublicChannels
description: Get all supergroups/channels where you're admin
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.getAdminedPublicChannels  
[Back to methods index](index.md)


Get all supergroups/channels where you're admin

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|by\_location|[Bool](../types/Bool.md) | Get channels by location | Optional|
|check\_limit|[Bool](../types/Bool.md) | Check limit | Optional|


### Return type: [messages\_Chats](../types/messages_Chats.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Chats = $MadelineProto->channels->getAdminedPublicChannels(['by_location' => Bool, 'check_limit' => Bool, ]);
```

Or, if you're into Lua:

```lua
messages_Chats = channels.getAdminedPublicChannels({by_location=Bool, check_limit=Bool, })
```

