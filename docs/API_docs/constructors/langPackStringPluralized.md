---
title: "langPackStringPluralized"
description: "A language pack string which has different forms based on the number of some object it mentions. See https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html for more info"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: langPackStringPluralized  
[Back to constructors index](/API_docs/constructors/index.html)



A language pack string which has different forms based on the number of some object it mentions. See [https://www.unicode.org/cldr/charts/latest/supplemental/language\_plural\_rules.html](https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html) for more info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|key|[string](/API_docs/types/string.html) | Yes|Localization key|
|zero\_value|[string](/API_docs/types/string.html) | Optional|Value for zero objects|
|one\_value|[string](/API_docs/types/string.html) | Optional|Value for one object|
|two\_value|[string](/API_docs/types/string.html) | Optional|Value for two objects|
|few\_value|[string](/API_docs/types/string.html) | Optional|Value for a few objects|
|many\_value|[string](/API_docs/types/string.html) | Optional|Value for many objects|
|other\_value|[string](/API_docs/types/string.html) | Yes|Default value|



### Type: [LangPackString](/API_docs/types/LangPackString.html)


### Example:

```
$langPackStringPluralized = ['_' => 'langPackStringPluralized', 'key' => 'string', 'zero_value' => 'string', 'one_value' => 'string', 'two_value' => 'string', 'few_value' => 'string', 'many_value' => 'string', 'other_value' => 'string'];
```  
