---
title: help.configSimple
description: Config simple
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_configSimple.html
---
# Constructor: help.configSimple  
[Back to constructors index](index.md)



Config simple

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](../types/int.md) | Yes|Date|
|expires|[int](../types/int.md) | Yes|Expires|
|rules|Array of [AccessPointRule](../types/AccessPointRule.md) | Yes|Rules|



### Type: [help.ConfigSimple](../types/help.ConfigSimple.md)


### Example:

```php
$help.configSimple = ['_' => 'help.configSimple', 'date' => int, 'expires' => int, 'rules' => [AccessPointRule, AccessPointRule]];
```  


Or, if you're into Lua:

```lua
help.configSimple={_='help.configSimple', date=int, expires=int, rules={AccessPointRule}}

```


