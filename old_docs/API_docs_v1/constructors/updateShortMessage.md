---
title: updateShortMessage
description: Info about a message sent to (received from) another user
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShortMessage  
[Back to constructors index](index.md)



Info about a message sent to (received from) another user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|The message ID|
|from\_id|[int](../types/int.md) | Yes|
|message|[string](../types/string.md) | Yes|The message|
|pts|[int](../types/int.md) | Yes|[PTS](https://core.telegram.org/api/updates)|
|date|[int](../types/int.md) | Yes|[date](https://core.telegram.org/api/updates)|
|seq|[int](../types/int.md) | Yes|



### Type: [Updates](../types/Updates.md)


### Example:

```php
$updateShortMessage = ['_' => 'updateShortMessage', 'id' => int, 'from_id' => int, 'message' => 'string', 'pts' => int, 'date' => int, 'seq' => int];
```  


Or, if you're into Lua:

```lua
updateShortMessage={_='updateShortMessage', id=int, from_id=int, message='string', pts=int, date=int, seq=int}

```


