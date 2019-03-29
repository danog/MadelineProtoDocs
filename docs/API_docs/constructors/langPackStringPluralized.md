---
title: langPackStringPluralized
description: Lang pack string pluralized
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: langPackStringPluralized  
[Back to constructors index](index.md)



Lang pack string pluralized

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|key|[string](../types/string.md) | Yes|Key|
|zero\_value|[string](../types/string.md) | Optional|Zero value|
|one\_value|[string](../types/string.md) | Optional|One value|
|two\_value|[string](../types/string.md) | Optional|Two value|
|few\_value|[string](../types/string.md) | Optional|Few value|
|many\_value|[string](../types/string.md) | Optional|Many value|
|other\_value|[string](../types/string.md) | Yes|Other value|



### Type: [LangPackString](../types/LangPackString.md)


### Example:

```php
$langPackStringPluralized = ['_' => 'langPackStringPluralized', 'key' => 'string', 'zero_value' => 'string', 'one_value' => 'string', 'two_value' => 'string', 'few_value' => 'string', 'many_value' => 'string', 'other_value' => 'string'];
```  


Or, if you're into Lua:

```lua
langPackStringPluralized={_='langPackStringPluralized', key='string', zero_value='string', one_value='string', two_value='string', few_value='string', many_value='string', other_value='string'}

```


