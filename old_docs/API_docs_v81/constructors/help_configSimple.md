---
title: help.configSimple
description: help_configSimple attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: help.configSimple  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|date|[int](../types/int.md) | Yes|
|expires|[int](../types/int.md) | Yes|
|rules|Array of [AccessPointRule](../types/AccessPointRule.md) | Yes|



### Type: [help\_ConfigSimple](../types/help_ConfigSimple.md)


### Example:

```
$help_configSimple = ['_' => 'help.configSimple', 'date' => int, 'expires' => int, 'rules' => [AccessPointRule, AccessPointRule]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "help.configSimple", "date": int, "expires": int, "rules": [AccessPointRule]}
```


Or, if you're into Lua:  


```
help_configSimple={_='help.configSimple', date=int, expires=int, rules={AccessPointRule}}

```


