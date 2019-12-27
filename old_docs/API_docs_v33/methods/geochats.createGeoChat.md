---
title: geochats.createGeoChat
description: Create geochat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: geochats.createGeoChat  
[Back to methods index](index.md)


Create geochat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|title|[string](../types/string.md) | Geochat title | Yes|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Geochat location | Optional|
|address|[string](../types/string.md) | Geochat address | Yes|
|venue|[string](../types/string.md) | Geochat venue  | Yes|


### Return type: [geochats.StatedMessage](../types/geochats.StatedMessage.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$geochats.StatedMessage = $MadelineProto->geochats->createGeoChat(['title' => 'string', 'geo_point' => InputGeoPoint, 'address' => 'string', 'venue' => 'string', ]);
```

Or, if you're into Lua:

```lua
geochats.StatedMessage = geochats.createGeoChat({title='string', geo_point=InputGeoPoint, address='string', venue='string', })
```

