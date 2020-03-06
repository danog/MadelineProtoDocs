---
title: channels.getInactiveChannels
description: channels.getInactiveChannels parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getInactiveChannels.html
---
# Method: channels.getInactiveChannels  
[Back to methods index](index.md)




### Return type: [messages.InactiveChats](../types/messages.InactiveChats.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.InactiveChats = $MadelineProto->channels->getInactiveChannels();
```

Or, if you're into Lua:

```lua
messages.InactiveChats = channels.getInactiveChannels({})
```

