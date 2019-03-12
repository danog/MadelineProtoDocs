---
title: geochats.getLocated
description: Get nearby geochats
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: geochats.getLocated  
[Back to methods index](index.md)


Get nearby geochats

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Current location | Optional|
|radius|[int](../types/int.md) | Radius | Yes|
|limit|[int](../types/int.md) | Number of results to return | Yes|


### Return type: [geochats\_Located](../types/geochats_Located.md)

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

$geochats_Located = $MadelineProto->geochats->getLocated(['geo_point' => InputGeoPoint, 'radius' => int, 'limit' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - geochats.getLocated
* params - `{"geo_point": InputGeoPoint, "radius": int, "limit": int, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/geochats.getLocated`

Parameters:

geo_point - Json encoded InputGeoPoint

radius - Json encoded int

limit - Json encoded int




Or, if you're into Lua:

```lua
geochats_Located = geochats.getLocated({geo_point=InputGeoPoint, radius=int, limit=int, })
```

