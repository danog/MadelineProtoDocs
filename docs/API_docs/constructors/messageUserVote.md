---
title: messageUserVote
description: messageUserVote attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageUserVote  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[int](../types/int.md) | Yes|
|option|[bytes](../types/bytes.md) | Yes|
|date|[int](../types/int.md) | Yes|



### Type: [MessageUserVote](../types/MessageUserVote.md)


### Example:

```php
$messageUserVote = ['_' => 'messageUserVote', 'user_id' => int, 'option' => 'bytes', 'date' => int];
```  


Or, if you're into Lua:

```lua
messageUserVote={_='messageUserVote', user_id=int, option='bytes', date=int}

```


