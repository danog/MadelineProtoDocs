---
title: destroy_session_ok
description: Destroy session ok
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: destroy\_session\_ok  
[Back to constructors index](index.md)



Destroy session ok

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|session\_id|[long](../types/long.md) | Yes|Session ID|



### Type: [DestroySessionRes](../types/DestroySessionRes.md)


### Example:

```php
$destroy_session_ok = ['_' => 'destroy_session_ok', 'session_id' => long];
```  


Or, if you're into Lua:

```lua
destroy_session_ok={_='destroy_session_ok', session_id=long}

```


