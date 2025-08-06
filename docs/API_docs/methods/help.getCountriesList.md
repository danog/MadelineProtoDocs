---
title: "help.getCountriesList"
description: "Get name, ISO code, localized name and phone codes/patterns of all available countries"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getCountriesList.html
---
# Method: help.getCountriesList
[Back to methods index](index.html)



Get name, ISO code, localized name and phone codes/patterns of all available countries

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|lang\_code|[string](/API_docs/types/string.html) | Language code of the current user | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) |  | Optional|


### Return type: [help.CountriesList](/API_docs/types/help.CountriesList.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help_CountriesList = $MadelineProto->help->getCountriesList(lang_code: 'string', hash: [$long\|string, $long\|string], );
```

