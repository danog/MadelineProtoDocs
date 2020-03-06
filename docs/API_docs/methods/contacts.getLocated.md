---
title: contacts.getLocated
description: Get contacts near you
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_getLocated.html
---
# Method: contacts.getLocated  
[Back to methods index](index.md)


Get contacts near you

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|background|[Bool](../types/Bool.md) |  | Optional|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Geolocation | Optional|
|self\_expires|[int](../types/int.md) |  | Optional|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->contacts->getLocated(['background' => Bool, 'geo_point' => InputGeoPoint, 'self_expires' => int, ]);
```

Or, if you're into Lua:

```lua
Updates = contacts.getLocated({background=Bool, geo_point=InputGeoPoint, self_expires=int, })
```

