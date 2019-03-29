---
title: phoneCall
description: Phone call
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneCall  
[Back to constructors index](index.md)



Phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|p2p\_allowed|[Bool](../types/Bool.md) | Optional|P2p allowed?|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|date|[int](../types/int.md) | Yes|Date|
|admin\_id|[int](../types/int.md) | Yes|Admin ID|
|participant\_id|[int](../types/int.md) | Yes|Participant ID|
|g\_a\_or\_b|[bytes](../types/bytes.md) | Yes|G a or b|
|key\_fingerprint|[long](../types/long.md) | Yes|Key fingerprint|
|protocol|[PhoneCallProtocol](../types/PhoneCallProtocol.md) | Yes|Protocol|
|connection|[PhoneConnection](../types/PhoneConnection.md) | Yes|Connection|
|alternative\_connections|Array of [PhoneConnection](../types/PhoneConnection.md) | Yes|Alternative connections|
|start\_date|[int](../types/int.md) | Yes|Start date|



### Type: [PhoneCall](../types/PhoneCall.md)


### Example:

```php
$phoneCall = ['_' => 'phoneCall', 'p2p_allowed' => Bool, 'id' => long, 'access_hash' => long, 'date' => int, 'admin_id' => int, 'participant_id' => int, 'g_a_or_b' => 'bytes', 'key_fingerprint' => long, 'protocol' => PhoneCallProtocol, 'connection' => PhoneConnection, 'alternative_connections' => [PhoneConnection, PhoneConnection], 'start_date' => int];
```  


Or, if you're into Lua:

```lua
phoneCall={_='phoneCall', p2p_allowed=Bool, id=long, access_hash=long, date=int, admin_id=int, participant_id=int, g_a_or_b='bytes', key_fingerprint=long, protocol=PhoneCallProtocol, connection=PhoneConnection, alternative_connections={PhoneConnection}, start_date=int}

```


