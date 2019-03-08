---
title: updateUserPinnedMessage
description: Update user pinned message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserPinnedMessage  
[Back to constructors index](index.md)



Update user pinned message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|id|[int](../types/int.md) | Yes|ID|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateUserPinnedMessage = ['_' => 'updateUserPinnedMessage', 'user_id' => int, 'id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateUserPinnedMessage", "user_id": int, "id": int}
```


Or, if you're into Lua:

```lua
updateUserPinnedMessage={_='updateUserPinnedMessage', user_id=int, id=int}

```


