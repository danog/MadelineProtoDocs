---
title: help.passportConfig
description: Telegram [passport](https://core.telegram.org/passport) configuration
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: help.passportConfig  
[Back to constructors index](index.md)



Telegram [passport](https://core.telegram.org/passport) configuration

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|[Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|countries\_langs|[DataJSON](../types/DataJSON.md) | Yes|Localization|



### Type: [help\_PassportConfig](../types/help_PassportConfig.md)


### Example:

```php
$help_passportConfig = ['_' => 'help.passportConfig', 'hash' => int, 'countries_langs' => DataJSON];
```  


Or, if you're into Lua:

```lua
help_passportConfig={_='help.passportConfig', hash=int, countries_langs=DataJSON}

```


