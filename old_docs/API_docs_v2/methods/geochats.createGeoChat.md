---
title: geochats.createGeoChat
description: geochats.createGeoChat parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/geochats_createGeoChat.html
---
# Method: geochats.createGeoChat
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|title|[string](../types/string.md) | Yes|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Optional|
|address|[string](../types/string.md) | Yes|
|venue|[string](../types/string.md) | Yes|


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

