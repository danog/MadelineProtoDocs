---
title: geochats.getLocated
description: geochats.getLocated parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/geochats_getLocated.html
---
# Method: geochats.getLocated
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Optional|
|radius|[int](../types/int.md) | Yes|
|limit|[int](../types/int.md) | Yes|


### Return type: [geochats.Located](../types/geochats.Located.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$geochats.Located = $MadelineProto->geochats->getLocated(['geo_point' => InputGeoPoint, 'radius' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
geochats.Located = geochats.getLocated({geo_point=InputGeoPoint, radius=int, limit=int, })
```

