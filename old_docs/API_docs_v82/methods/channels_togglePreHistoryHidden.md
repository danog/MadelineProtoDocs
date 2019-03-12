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

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->channels->togglePreHistoryHidden(['channel' => InputChannel, 'enabled' => Bool, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - channels.togglePreHistoryHidden
* params - `{"channel": InputChannel, "enabled": Bool, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/channels.togglePreHistoryHidden`

Parameters:

channel - Json encoded InputChannel

enabled - Json encoded Bool




Or, if you're into Lua:

```lua
Updates = channels.togglePreHistoryHidden({channel=InputChannel, enabled=Bool, })
```

