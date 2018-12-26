---
title: destroy_session_none
description: Destroy session none
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: destroy\_session\_none  
[Back to constructors index](index.md)



Destroy session none

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|session\_id|[long](../types/long.md) | Yes|Session ID|



### Type: [DestroySessionRes](../types/DestroySessionRes.md)


### Example:

```php
$destroy_session_none = ['_' => 'destroy_session_none', 'session_id' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "destroy_session_none", "session_id": long}
```


Or, if you're into Lua:

```lua
destroy_session_none={_='destroy_session_none', session_id=long}

```


