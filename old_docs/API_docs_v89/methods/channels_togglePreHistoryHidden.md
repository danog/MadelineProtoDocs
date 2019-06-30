---
title: channels.togglePreHistoryHidden
description: Enable or disable hidden history for new channel/supergroup users
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.togglePreHistoryHidden  
[Back to methods index](index.md)


Enable or disable hidden history for new channel/supergroup users

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel/supergroup | Optional|
|enabled|[Bool](../types/Bool.md) | Enable or disable hidden history for new channel/supergroup users | Yes|


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

$Updates = $MadelineProto->channels->togglePreHistoryHidden(['channel' => InputChannel, 'enabled' => Bool, ]);
```

Or, if you're into Lua:

```lua
Updates = channels.togglePreHistoryHidden({channel=InputChannel, enabled=Bool, })
```

