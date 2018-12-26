---
title: geochats.getRecents
description: Get recent geochats
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: geochats.getRecents  
[Back to methods index](index.md)


Get recent geochats

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|offset|[int](../types/int.md) | Offset | Yes|
|limit|[int](../types/int.md) | Number of results to return | Yes|


### Return type: [geochats\_Messages](../types/geochats_Messages.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$geochats_Messages = $MadelineProto->geochats->getRecents(['offset' => int, 'limit' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - geochats.getRecents
* params - `{"offset": int, "limit": int, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/geochats.getRecents`

Parameters:

offset - Json encoded int

limit - Json encoded int




Or, if you're into Lua:

```lua
geochats_Messages = geochats.getRecents({offset=int, limit=int, })
```

