---
title: updateUserPinnedMessage
description: A message was pinned in a private chat with a user
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserPinnedMessage  
[Back to constructors index](index.md)



A message was pinned in a private chat with a user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User that pinned the message|
|id|[int](../types/int.md) | Yes|Message ID that was pinned|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateUserPinnedMessage = ['_' => 'updateUserPinnedMessage', 'user_id' => int, 'id' => int];
```  


Or, if you're into Lua:

```lua
updateUserPinnedMessage={_='updateUserPinnedMessage', user_id=int, id=int}

```


