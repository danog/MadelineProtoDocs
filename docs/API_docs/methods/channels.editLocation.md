---
title: "channels.editLocation"
description: "Edit location of geogroup"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_editLocation.html
---
# Method: channels.editLocation
[Back to methods index](index.md)



Edit location of geogroup

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | [Geogroup](https://core.telegram.org/api/channel) | Optional|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | New geolocation | Optional|
|address|[string](../types/string.md) | Address string | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


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

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MEGAGROUP_REQUIRED|You can only use this method on a supergroup|


