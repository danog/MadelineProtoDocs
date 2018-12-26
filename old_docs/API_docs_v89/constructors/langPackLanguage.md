---
title: langPackLanguage
description: Lang pack language
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: langPackLanguage  
[Back to constructors index](index.md)



Lang pack language

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|official|[Bool](../types/Bool.md) | Optional|Official?|
|rtl|[Bool](../types/Bool.md) | Optional|Rtl?|
|name|[string](../types/string.md) | Yes|Name|
|native\_name|[string](../types/string.md) | Yes|Native name|
|lang\_code|[string](../types/string.md) | Yes|Lang code|
|base\_lang\_code|[string](../types/string.md) | Optional|Base lang code|
|plural\_code|[string](../types/string.md) | Yes|Plural code|
|strings\_count|[int](../types/int.md) | Yes|Strings count|
|translated\_count|[int](../types/int.md) | Yes|Translated count|
|translations\_url|[string](../types/string.md) | Yes|Translations URL|



### Type: [LangPackLanguage](../types/LangPackLanguage.md)


### Example:

```php
$langPackLanguage = ['_' => 'langPackLanguage', 'official' => Bool, 'rtl' => Bool, 'name' => 'string', 'native_name' => 'string', 'lang_code' => 'string', 'base_lang_code' => 'string', 'plural_code' => 'string', 'strings_count' => int, 'translated_count' => int, 'translations_url' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "langPackLanguage", "official": Bool, "rtl": Bool, "name": "string", "native_name": "string", "lang_code": "string", "base_lang_code": "string", "plural_code": "string", "strings_count": int, "translated_count": int, "translations_url": "string"}
```


Or, if you're into Lua:

```lua
langPackLanguage={_='langPackLanguage', official=Bool, rtl=Bool, name='string', native_name='string', lang_code='string', base_lang_code='string', plural_code='string', strings_count=int, translated_count=int, translations_url='string'}

```


