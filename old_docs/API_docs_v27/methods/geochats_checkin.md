---
title: geochats.checkin
description: Join a geochat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: geochats.checkin  
[Back to methods index](index.md)


Join a geochat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[InputGeoChat](../types/InputGeoChat.md) | The geochat | Yes|


### Return type: [geochats\_StatedMessage](../types/geochats_StatedMessage.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$geochats_StatedMessage = $MadelineProto->geochats->checkin(['peer' => InputGeoChat, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - geochats.checkin
* params - `{"peer": InputGeoChat, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/geochats.checkin`

Parameters:

peer - Json encoded InputGeoChat




Or, if you're into Lua:

```lua
geochats_StatedMessage = geochats.checkin({peer=InputGeoChat, })
```

