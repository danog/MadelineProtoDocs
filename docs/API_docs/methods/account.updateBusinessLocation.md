---
title: "account.updateBusinessLocation"
description: "[Businesses »](https://core.telegram.org/api/business#location) may advertise their location using this method, see [here »](https://core.telegram.org/api/business#location) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_updateBusinessLocation.html
---
# Method: account.updateBusinessLocation
[Back to methods index](index.html)



[Businesses »](https://core.telegram.org/api/business#location) may advertise their location using this method, see [here »](https://core.telegram.org/api/business#location) for more info.

To remove business location information invoke the method without setting any of the parameters.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|geo\_point|[InputGeoPoint](/API_docs/types/InputGeoPoint.html) | Optional, contains a set of geographical coordinates. | Optional|
|address|[string](/API_docs/types/string.html) | Mandatory when setting/updating the location, contains a textual description of the address (max 96 UTF-8 chars). | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->updateBusinessLocation(geo_point: $InputGeoPoint, address: 'string', );
```

