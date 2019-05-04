---
title: channels.getAdminedPublicChannels
description: Get all supergroups/channels where you're admin
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.getAdminedPublicChannels  
[Back to methods index](index.md)


Get all supergroups/channels where you're admin



### Return type: [messages\_Chats](../types/messages_Chats.md)

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

$messages_Chats = $MadelineProto->channels->getAdminedPublicChannels();
```

Or, if you're into Lua:

```lua
messages_Chats = channels.getAdminedPublicChannels({})
```

