---
title: langPackLanguage
description: Identifies a localization pack
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: langPackLanguage  
[Back to constructors index](index.md)



Identifies a localization pack

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|name|[string](../types/string.md) | Yes|Language name|
|native\_name|[string](../types/string.md) | Yes|Language name in the language itself|
|lang\_code|[string](../types/string.md) | Yes|Language code (pack identifier)|



### Type: [LangPackLanguage](../types/LangPackLanguage.md)


### Example:

```php
$langPackLanguage = ['_' => 'langPackLanguage', 'name' => 'string', 'native_name' => 'string', 'lang_code' => 'string'];
```  


Or, if you're into Lua:

```lua
langPackLanguage={_='langPackLanguage', name='string', native_name='string', lang_code='string'}

```


