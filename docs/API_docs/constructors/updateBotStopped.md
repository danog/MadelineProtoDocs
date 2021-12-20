---
title: "updateBotStopped"
description: "updateBotStopped attributes, type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotStopped  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[long](../types/long.md) | Yes|
|date|[int](../types/int.md) | Yes|
|stopped|[Bool](../types/Bool.md) | Yes|
|qts|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateBotStopped = ['_' => 'updateBotStopped', 'user_id' => long, 'date' => int, 'stopped' => Bool, 'qts' => int];
```  


Or, if you're into Lua:

```lua
updateBotStopped={_='updateBotStopped', user_id=long, date=int, stopped=Bool, qts=int}

```


