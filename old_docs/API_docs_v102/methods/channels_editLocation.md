---
title: channels.editLocation
description: Edit location (geochats)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.editLocation  
[Back to methods index](index.md)


Edit location (geochats)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Channel | Optional|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Geo point | Optional|
|address|[string](../types/string.md) | Physical location (geochats) | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->channels->editLocation(['channel' => InputChannel, 'geo_point' => InputGeoPoint, 'address' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = channels.editLocation({channel=InputChannel, geo_point=InputGeoPoint, address='string', })
```

