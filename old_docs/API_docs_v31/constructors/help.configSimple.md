---
title: help.configSimple
description: help.configSimple attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_configSimple.html
---
# Constructor: help.configSimple  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|date|[int](../types/int.md) | Yes|
|expires|[int](../types/int.md) | Yes|
|rules|Array of [AccessPointRule](../types/AccessPointRule.md) | Yes|



### Type: [help.ConfigSimple](../types/help.ConfigSimple.md)


### Example:

```php
$help.configSimple = ['_' => 'help.configSimple', 'date' => int, 'expires' => int, 'rules' => [AccessPointRule, AccessPointRule]];
```  


Or, if you're into Lua:

```lua
help.configSimple={_='help.configSimple', date=int, expires=int, rules={AccessPointRule}}

```


