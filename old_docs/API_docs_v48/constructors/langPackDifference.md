---
title: langPackDifference
description: Changes to the app's localization pack
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: langPackDifference  
[Back to constructors index](index.md)



Changes to the app's localization pack

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|lang\_code|[string](../types/string.md) | Yes|Language code|
|from\_version|[int](../types/int.md) | Yes|Previous version number|
|version|[int](../types/int.md) | Yes|New version number|
|strings|Array of [LangPackString](../types/LangPackString.md) | Yes|Localized strings|



### Type: [LangPackDifference](../types/LangPackDifference.md)


### Example:

```php
$langPackDifference = ['_' => 'langPackDifference', 'lang_code' => 'string', 'from_version' => int, 'version' => int, 'strings' => [LangPackString, LangPackString]];
```  


Or, if you're into Lua:

```lua
langPackDifference={_='langPackDifference', lang_code='string', from_version=int, version=int, strings={LangPackString}}

```


