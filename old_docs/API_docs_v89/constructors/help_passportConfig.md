---
title: help.passportConfig
description: Passport config
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: help.passportConfig  
[Back to constructors index](index.md)



Passport config

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|Hash|
|countries\_langs|[DataJSON](../types/DataJSON.md) | Yes|Countries langs|



### Type: [help\_PassportConfig](../types/help_PassportConfig.md)


### Example:

```php
$help_passportConfig = ['_' => 'help.passportConfig', 'hash' => int, 'countries_langs' => DataJSON];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "help.passportConfig", "hash": int, "countries_langs": DataJSON}
```


Or, if you're into Lua:

```lua
help_passportConfig={_='help.passportConfig', hash=int, countries_langs=DataJSON}

```


