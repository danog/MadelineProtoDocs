---
title: "langPackLanguage"
description: "Identifies a localization pack"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: langPackLanguage  
[Back to constructors index](index.md)



Identifies a localization pack

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|official|[Bool](../types/Bool.md) | Optional|Whether the language pack is official|
|rtl|[Bool](../types/Bool.md) | Optional|Is this a localization pack for an RTL language|
|beta|[Bool](../types/Bool.md) | Optional|Is this a beta localization pack?|
|name|[string](../types/string.md) | Yes|Language name|
|native\_name|[string](../types/string.md) | Yes|Language name in the language itself|
|lang\_code|[string](../types/string.md) | Yes|Language code (pack identifier)|
|base\_lang\_code|[string](../types/string.md) | Optional|Identifier of a base language pack; may be empty. If a string is missed in the language pack, then it should be fetched from base language pack. Unsupported in custom language packs|
|plural\_code|[string](../types/string.md) | Yes|A language code to be used to apply plural forms. See [https://www.unicode.org/cldr/charts/latest/supplemental/language\_plural\_rules.html](https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html) for more info|
|strings\_count|[int](../types/int.md) | Yes|Total number of non-deleted strings from the language pack|
|translated\_count|[int](../types/int.md) | Yes|Total number of translated strings from the language pack|
|translations\_url|[string](../types/string.md) | Yes|Link to language translation interface; empty for custom local language packs|



### Type: [LangPackLanguage](../types/LangPackLanguage.md)


### Example:

```php
$langPackLanguage = ['_' => 'langPackLanguage', 'official' => Bool, 'rtl' => Bool, 'beta' => Bool, 'name' => 'string', 'native_name' => 'string', 'lang_code' => 'string', 'base_lang_code' => 'string', 'plural_code' => 'string', 'strings_count' => int, 'translated_count' => int, 'translations_url' => 'string'];
```  


Or, if you're into Lua:

```lua
langPackLanguage={_='langPackLanguage', official=Bool, rtl=Bool, beta=Bool, name='string', native_name='string', lang_code='string', base_lang_code='string', plural_code='string', strings_count=int, translated_count=int, translations_url='string'}

```


