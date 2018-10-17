---
title: langPackLanguage
description: langPackLanguage attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: langPackLanguage  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|name|[string](../types/string.md) | Yes|
|native\_name|[string](../types/string.md) | Yes|
|lang\_code|[string](../types/string.md) | Yes|



### Type: [LangPackLanguage](../types/LangPackLanguage.md)


### Example:

```php
$langPackLanguage = ['_' => 'langPackLanguage', 'name' => 'string', 'native_name' => 'string', 'lang_code' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "langPackLanguage", "name": "string", "native_name": "string", "lang_code": "string"}
```


Or, if you're into Lua:

```lua
langPackLanguage={_='langPackLanguage', name='string', native_name='string', lang_code='string'}

```


