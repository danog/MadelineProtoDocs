---
title: "messageUserVote"
description: "How a user voted in a poll"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageUserVote  
[Back to constructors index](index.md)



How a user voted in a poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](../types/long.md) | Yes|
|option|[bytes](../types/bytes.md) | Yes|The option chosen by the user|
|date|[int](../types/int.md) | Yes|When did the user cast the vote|



### Type: [MessageUserVote](../types/MessageUserVote.md)


### Example:

```php
$messageUserVote = ['_' => 'messageUserVote', 'user_id' => long, 'option' => 'bytes', 'date' => int];
```  


Or, if you're into Lua:

```lua
messageUserVote={_='messageUserVote', user_id=long, option='bytes', date=int}

```


