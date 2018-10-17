---
title: langPackDifference
description: langPackDifference attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: langPackDifference  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|lang\_code|[string](../types/string.md) | Yes|
|from\_version|[int](../types/int.md) | Yes|
|version|[int](../types/int.md) | Yes|
|strings|Array of [LangPackString](../types/LangPackString.md) | Yes|



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


