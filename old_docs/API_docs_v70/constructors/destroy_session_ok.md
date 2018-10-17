---
title: destroy_session_ok
description: destroy_session_ok attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: destroy\_session\_ok  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|session\_id|[long](../types/long.md) | Yes|



### Type: [DestroySessionRes](../types/DestroySessionRes.md)


### Example:

```php
$destroy_session_ok = ['_' => 'destroy_session_ok', 'session_id' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "destroy_session_ok", "session_id": long}
```


Or, if you're into Lua:

```lua
destroy_session_ok={_='destroy_session_ok', session_id=long}

```


