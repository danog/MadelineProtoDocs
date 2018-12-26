---
title: accessPointRule
description: Access point rule
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: accessPointRule  
[Back to constructors index](index.md)



Access point rule

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_prefix\_rules|[string](../types/string.md) | Yes|Phone prefix rules|
|dc\_id|[int](../types/int.md) | Yes|DC ID|
|ips|Array of [IpPort](../types/IpPort.md) | Yes|Ips|



### Type: [AccessPointRule](../types/AccessPointRule.md)


### Example:

```php
$accessPointRule = ['_' => 'accessPointRule', 'phone_prefix_rules' => 'string', 'dc_id' => int, 'ips' => [IpPort, IpPort]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "accessPointRule", "phone_prefix_rules": "string", "dc_id": int, "ips": [IpPort]}
```


Or, if you're into Lua:

```lua
accessPointRule={_='accessPointRule', phone_prefix_rules='string', dc_id=int, ips={IpPort}}

```


