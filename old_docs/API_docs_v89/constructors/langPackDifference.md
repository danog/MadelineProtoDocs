---
title: langPackDifference
description: Lang pack difference
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: langPackDifference  
[Back to constructors index](index.md)



Lang pack difference

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|lang\_code|[string](../types/string.md) | Yes|Lang code|
|from\_version|[int](../types/int.md) | Yes|From version|
|version|[int](../types/int.md) | Yes|Version|
|strings|Array of [LangPackString](../types/LangPackString.md) | Yes|Strings|



### Type: [LangPackDifference](../types/LangPackDifference.md)


### Example:

```php
$langPackDifference = ['_' => 'langPackDifference', 'lang_code' => 'string', 'from_version' => int, 'version' => int, 'strings' => [LangPackString, LangPackString]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "langPackDifference", "lang_code": "string", "from_version": int, "version": int, "strings": [LangPackString]}
```


Or, if you're into Lua:

```lua
langPackDifference={_='langPackDifference', lang_code='string', from_version=int, version=int, strings={LangPackString}}

```


