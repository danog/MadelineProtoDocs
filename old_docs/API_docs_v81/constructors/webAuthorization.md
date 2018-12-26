---
title: webAuthorization
description: Web authorization
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webAuthorization  
[Back to constructors index](index.md)



Web authorization

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](../types/long.md) | Yes|Hash|
|bot\_id|[int](../types/int.md) | Yes|Bot ID|
|domain|[string](../types/string.md) | Yes|Domain|
|browser|[string](../types/string.md) | Yes|Browser|
|platform|[string](../types/string.md) | Yes|Platform|
|date\_created|[int](../types/int.md) | Yes|Date created|
|date\_active|[int](../types/int.md) | Yes|Date active|
|ip|[string](../types/string.md) | Yes|Ip|
|region|[string](../types/string.md) | Yes|Region|



### Type: [WebAuthorization](../types/WebAuthorization.md)


### Example:

```php
$webAuthorization = ['_' => 'webAuthorization', 'hash' => long, 'bot_id' => int, 'domain' => 'string', 'browser' => 'string', 'platform' => 'string', 'date_created' => int, 'date_active' => int, 'ip' => 'string', 'region' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "webAuthorization", "hash": long, "bot_id": int, "domain": "string", "browser": "string", "platform": "string", "date_created": int, "date_active": int, "ip": "string", "region": "string"}
```


Or, if you're into Lua:

```lua
webAuthorization={_='webAuthorization', hash=long, bot_id=int, domain='string', browser='string', platform='string', date_created=int, date_active=int, ip='string', region='string'}

```


