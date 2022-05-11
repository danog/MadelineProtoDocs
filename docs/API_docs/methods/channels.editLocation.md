---
title: "channels.editLocation"
description: "Edit location of geogroup"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_editLocation.html
---
# Method: channels.editLocation
[Back to methods index](index.html)



Edit location of geogroup

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | [Geogroup](https://core.telegram.org/api/channel) | Optional|
|geo\_point|[InputGeoPoint](/API_docs/types/InputGeoPoint.html) | New geolocation | Optional|
|address|[string](/API_docs/types/string.html) | Address string | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Bool = $MadelineProto->channels->editLocation(channel: InputChannel, geo_point: InputGeoPoint, address: 'string', );
```

