---
title: "langPackLanguage"
description: "Identifies a localization pack"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: langPackLanguage  
[Back to constructors index](/API_docs/constructors/index.html)



Identifies a localization pack

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|official|[Bool](/API_docs/types/Bool.html) | Optional|Whether the language pack is official|
|rtl|[Bool](/API_docs/types/Bool.html) | Optional|Is this a localization pack for an RTL language|
|beta|[Bool](/API_docs/types/Bool.html) | Optional|Is this a beta localization pack?|
|name|[string](/API_docs/types/string.html) | Yes|Language name|
|native\_name|[string](/API_docs/types/string.html) | Yes|Language name in the language itself|
|lang\_code|[string](/API_docs/types/string.html) | Yes|Language code (pack identifier)|
|base\_lang\_code|[string](/API_docs/types/string.html) | Optional|Identifier of a base language pack; may be empty. If a string is missed in the language pack, then it should be fetched from base language pack. Unsupported in custom language packs|
|plural\_code|[string](/API_docs/types/string.html) | Yes|A language code to be used to apply plural forms. See [https://www.unicode.org/cldr/charts/latest/supplemental/language\_plural\_rules.html](https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html) for more info|
|strings\_count|[int](/API_docs/types/int.html) | Yes|Total number of non-deleted strings from the language pack|
|translated\_count|[int](/API_docs/types/int.html) | Yes|Total number of translated strings from the language pack|
|translations\_url|[string](/API_docs/types/string.html) | Yes|Link to language translation interface; empty for custom local language packs|



### Type: [LangPackLanguage](/API_docs/types/LangPackLanguage.html)


### Example:

```
$langPackLanguage = ['_' => 'langPackLanguage', 'official' => Bool, 'rtl' => Bool, 'beta' => Bool, 'name' => 'string', 'native_name' => 'string', 'lang_code' => 'string', 'base_lang_code' => 'string', 'plural_code' => 'string', 'strings_count' => int, 'translated_count' => int, 'translations_url' => 'string'];
```  
