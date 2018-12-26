---
title: authorization
description: Authorization
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: authorization  
[Back to constructors index](index.md)



Authorization

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|current|[Bool](../types/Bool.md) | Optional|Current?|
|official\_app|[Bool](../types/Bool.md) | Optional|Official app?|
|password\_pending|[Bool](../types/Bool.md) | Optional|Password pending?|
|hash|[long](../types/long.md) | Yes|Hash|
|device\_model|[string](../types/string.md) | Yes|Device model|
|platform|[string](../types/string.md) | Yes|Platform|
|system\_version|[string](../types/string.md) | Yes|System version|
|api\_id|[int](../types/int.md) | Yes|Api ID|
|app\_name|[string](../types/string.md) | Yes|App name|
|app\_version|[string](../types/string.md) | Yes|App version|
|date\_created|[int](../types/int.md) | Yes|Date created|
|date\_active|[int](../types/int.md) | Yes|Date active|
|ip|[string](../types/string.md) | Yes|Ip|
|country|[string](../types/string.md) | Yes|Country|
|region|[string](../types/string.md) | Yes|Region|



### Type: [Authorization](../types/Authorization.md)


### Example:

```php
$authorization = ['_' => 'authorization', 'current' => Bool, 'official_app' => Bool, 'password_pending' => Bool, 'hash' => long, 'device_model' => 'string', 'platform' => 'string', 'system_version' => 'string', 'api_id' => int, 'app_name' => 'string', 'app_version' => 'string', 'date_created' => int, 'date_active' => int, 'ip' => 'string', 'country' => 'string', 'region' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "authorization", "current": Bool, "official_app": Bool, "password_pending": Bool, "hash": long, "device_model": "string", "platform": "string", "system_version": "string", "api_id": int, "app_name": "string", "app_version": "string", "date_created": int, "date_active": int, "ip": "string", "country": "string", "region": "string"}
```


Or, if you're into Lua:

```lua
authorization={_='authorization', current=Bool, official_app=Bool, password_pending=Bool, hash=long, device_model='string', platform='string', system_version='string', api_id=int, app_name='string', app_version='string', date_created=int, date_active=int, ip='string', country='string', region='string'}

```


