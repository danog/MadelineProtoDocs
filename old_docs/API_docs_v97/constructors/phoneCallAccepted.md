---
title: phoneCallAccepted
description: Phone call accepted
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneCallAccepted  
[Back to constructors index](index.md)



Phone call accepted

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|date|[int](../types/int.md) | Yes|Date|
|admin\_id|[int](../types/int.md) | Yes|Admin ID|
|participant\_id|[int](../types/int.md) | Yes|Participant ID|
|g\_b|[bytes](../types/bytes.md) | Yes|G b|
|protocol|[PhoneCallProtocol](../types/PhoneCallProtocol.md) | Yes|Protocol|



### Type: [PhoneCall](../types/PhoneCall.md)


### Example:

```php
$phoneCallAccepted = ['_' => 'phoneCallAccepted', 'id' => long, 'access_hash' => long, 'date' => int, 'admin_id' => int, 'participant_id' => int, 'g_b' => 'bytes', 'protocol' => PhoneCallProtocol];
```  


Or, if you're into Lua:

```lua
phoneCallAccepted={_='phoneCallAccepted', id=long, access_hash=long, date=int, admin_id=int, participant_id=int, g_b='bytes', protocol=PhoneCallProtocol}

```


