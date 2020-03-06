---
title: updateMessagePollVote
description: updateMessagePollVote attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMessagePollVote  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|poll\_id|[long](../types/long.md) | Yes|
|user\_id|[int](../types/int.md) | Yes|
|options|Array of [bytes](../types/bytes.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateMessagePollVote = ['_' => 'updateMessagePollVote', 'poll_id' => long, 'user_id' => int, 'options' => ['bytes', 'bytes']];
```  


Or, if you're into Lua:

```lua
updateMessagePollVote={_='updateMessagePollVote', poll_id=long, user_id=int, options={'bytes'}}

```


