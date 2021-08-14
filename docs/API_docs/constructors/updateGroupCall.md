---
title: updateGroupCall
description: updateGroupCall attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateGroupCall  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat\_id|[int](../types/int.md) | Yes|
|call|[GroupCall](../types/GroupCall.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateGroupCall = ['_' => 'updateGroupCall', 'chat_id' => int, 'call' => GroupCall];
```  


Or, if you're into Lua:

```lua
updateGroupCall={_='updateGroupCall', chat_id=int, call=GroupCall}

```


