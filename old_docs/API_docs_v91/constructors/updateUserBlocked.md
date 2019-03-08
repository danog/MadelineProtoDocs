---
title: updateUserBlocked
description: Update user blocked
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserBlocked  
[Back to constructors index](index.md)



Update user blocked

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|blocked|[Bool](../types/Bool.md) | Yes|Blocked?|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateUserBlocked = ['_' => 'updateUserBlocked', 'user_id' => int, 'blocked' => Bool];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateUserBlocked", "user_id": int, "blocked": Bool}
```


Or, if you're into Lua:

```lua
updateUserBlocked={_='updateUserBlocked', user_id=int, blocked=Bool}

```


