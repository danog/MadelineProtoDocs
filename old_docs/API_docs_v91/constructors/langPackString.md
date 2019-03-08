---
title: langPackString
description: Lang pack string
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: langPackString  
[Back to constructors index](index.md)



Lang pack string

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|key|[string](../types/string.md) | Yes|Key|
|value|[string](../types/string.md) | Yes|Value|



### Type: [LangPackString](../types/LangPackString.md)


### Example:

```php
$langPackString = ['_' => 'langPackString', 'key' => 'string', 'value' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "langPackString", "key": "string", "value": "string"}
```


Or, if you're into Lua:

```lua
langPackString={_='langPackString', key='string', value='string'}

```


