---
title: langPackString
description: langPackString attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: langPackString  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|key|[string](../types/string.md) | Yes|
|value|[string](../types/string.md) | Yes|



### Type: [LangPackString](../types/LangPackString.md)


### Example:

```
$langPackString = ['_' => 'langPackString', 'key' => 'string', 'value' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "langPackString", "key": "string", "value": "string"}
```


Or, if you're into Lua:  


```
langPackString={_='langPackString', key='string', value='string'}

```


