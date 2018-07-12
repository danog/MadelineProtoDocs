---
title: accessPointRule
description: accessPointRule attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: accessPointRule  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|phone\_prefix\_rules|[string](../types/string.md) | Yes|
|dc\_id|[int](../types/int.md) | Yes|
|ips|Array of [IpPort](../types/IpPort.md) | Yes|



### Type: [AccessPointRule](../types/AccessPointRule.md)


### Example:

```
$accessPointRule = ['_' => 'accessPointRule', 'phone_prefix_rules' => 'string', 'dc_id' => int, 'ips' => [IpPort, IpPort]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "accessPointRule", "phone_prefix_rules": "string", "dc_id": int, "ips": [IpPort]}
```


Or, if you're into Lua:  


```
accessPointRule={_='accessPointRule', phone_prefix_rules='string', dc_id=int, ips={IpPort}}

```


