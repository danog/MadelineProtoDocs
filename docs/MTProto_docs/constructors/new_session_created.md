---
title: new_session_created
description: New session created
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: new\_session\_created  
[Back to constructors index](index.md)



New session created

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|first\_msg\_id|[long](../types/long.md) | Yes|First msg ID|
|unique\_id|[long](../types/long.md) | Yes|Unique ID|
|server\_salt|[long](../types/long.md) | Yes|Server salt|



### Type: [NewSession](../types/NewSession.md)


### Example:

```php
$new_session_created = ['_' => 'new_session_created', 'first_msg_id' => long, 'unique_id' => long, 'server_salt' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "new_session_created", "first_msg_id": long, "unique_id": long, "server_salt": long}
```


Or, if you're into Lua:

```lua
new_session_created={_='new_session_created', first_msg_id=long, unique_id=long, server_salt=long}

```


