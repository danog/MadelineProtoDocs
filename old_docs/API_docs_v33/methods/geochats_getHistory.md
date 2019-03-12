---
title: geochats.getHistory
description: Get geochat history
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: geochats.getHistory  
[Back to methods index](index.md)


Get geochat history

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[InputGeoChat](../types/InputGeoChat.md) | The geochat | Yes|
|offset|[int](../types/int.md) | Offset | Yes|
|max\_id|[int](../types/int.md) | Maximum message ID | Yes|
|limit|[int](../types/int.md) | Number of results to return | Yes|


### Return type: [geochats\_Messages](../types/geochats_Messages.md)

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

$geochats_Messages = $MadelineProto->geochats->getHistory(['peer' => InputGeoChat, 'offset' => int, 'max_id' => int, 'limit' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - geochats.getHistory
* params - `{"peer": InputGeoChat, "offset": int, "max_id": int, "limit": int, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/geochats.getHistory`

Parameters:

peer - Json encoded InputGeoChat

offset - Json encoded int

max_id - Json encoded int

limit - Json encoded int




Or, if you're into Lua:

```lua
geochats_Messages = geochats.getHistory({peer=InputGeoChat, offset=int, max_id=int, limit=int, })
```

