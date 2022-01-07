---
title: "langPackDifference"
description: "Changes to the app's localization pack"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: langPackDifference  
[Back to constructors index](/API_docs/constructors/index.md)



Changes to the app's localization pack

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|lang\_code|[string](/API_docs/types/string.md) | Yes|Language code|
|from\_version|[int](/API_docs/types/int.md) | Yes|Previous version number|
|version|[int](/API_docs/types/int.md) | Yes|New version number|
|strings|Array of [LangPackString](/API_docs/types/LangPackString.md) | Yes|Localized strings|



### Type: [LangPackDifference](/API_docs/types/LangPackDifference.md)


### Example:

```php
$langPackDifference = ['_' => 'langPackDifference', 'lang_code' => 'string', 'from_version' => int, 'version' => int, 'strings' => [LangPackString, LangPackString]];
```  
