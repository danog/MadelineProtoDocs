---
title: "help.getCountriesList"
description: "Get name, ISO code, localized name and phone codes/patterns of all available countries"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getCountriesList.html
---
# Method: help.getCountriesList
[Back to methods index](index.md)



Get name, ISO code, localized name and phone codes/patterns of all available countries

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|lang\_code|[string](../types/string.md) | Language code of the current user | Yes|
|hash|Array of [int](../types/int.md) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [help.CountriesList](../types/help.CountriesList.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help_CountriesList = $MadelineProto->help->getCountriesList(['lang_code' => 'string', 'hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
help_CountriesList = help.getCountriesList({lang_code='string', hash={int}, })
```

