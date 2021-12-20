---
title: "langPackStringPluralized"
description: "A language pack string which has different forms based on the number of some object it mentions. See https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html for more info"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: langPackStringPluralized  
[Back to constructors index](index.md)



A language pack string which has different forms based on the number of some object it mentions. See [https://www.unicode.org/cldr/charts/latest/supplemental/language\_plural\_rules.html](https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html) for more info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|key|[string](../types/string.md) | Yes|Localization key|
|zero\_value|[string](../types/string.md) | Optional|Value for zero objects|
|one\_value|[string](../types/string.md) | Optional|Value for one object|
|two\_value|[string](../types/string.md) | Optional|Value for two objects|
|few\_value|[string](../types/string.md) | Optional|Value for a few objects|
|many\_value|[string](../types/string.md) | Optional|Value for many objects|
|other\_value|[string](../types/string.md) | Yes|Default value|



### Type: [LangPackString](../types/LangPackString.md)


### Example:

```php
$langPackStringPluralized = ['_' => 'langPackStringPluralized', 'key' => 'string', 'zero_value' => 'string', 'one_value' => 'string', 'two_value' => 'string', 'few_value' => 'string', 'many_value' => 'string', 'other_value' => 'string'];
```  


Or, if you're into Lua:

```lua
langPackStringPluralized={_='langPackStringPluralized', key='string', zero_value='string', one_value='string', two_value='string', few_value='string', many_value='string', other_value='string'}

```


