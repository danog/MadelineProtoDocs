---
title: help.getCountriesList
description: help.getCountriesList parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getCountriesList.html
---
# Method: help.getCountriesList
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|lang\_code|[string](../types/string.md) | Yes|
|hash|Array of [int](../types/int.md) | Optional|


### Return type: [help.CountriesList](../types/help.CountriesList.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help.CountriesList = $MadelineProto->help->getCountriesList(['lang_code' => 'string', 'hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
help.CountriesList = help.getCountriesList({lang_code='string', hash={int}, })
```

