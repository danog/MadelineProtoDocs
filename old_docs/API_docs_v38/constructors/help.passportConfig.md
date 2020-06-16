---
title: help.passportConfig
description: Telegram [passport](https://core.telegram.org/passport) configuration
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_passportConfig.html
---
# Constructor: help.passportConfig  
[Back to constructors index](index.md)



Telegram [passport](https://core.telegram.org/passport) configuration

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|
|countries\_langs|[DataJSON](../types/DataJSON.md) | Yes|Localization|



### Type: [help.PassportConfig](../types/help.PassportConfig.md)


### Example:

```php
$help.passportConfig = ['_' => 'help.passportConfig', 'hash' => int, 'countries_langs' => DataJSON];
```  


Or, if you're into Lua:

```lua
help.passportConfig={_='help.passportConfig', hash=int, countries_langs=DataJSON}

```


