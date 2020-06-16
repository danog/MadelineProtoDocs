---
title: updateMessagePollVote
description: A specific user has voted in a poll
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMessagePollVote  
[Back to constructors index](index.md)



A specific user has voted in a poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|poll\_id|[long](../types/long.md) | Yes|Poll ID|
|user\_id|[int](../types/int.md) | Yes|User ID|
|options|Array of [bytes](../types/bytes.md) | Yes|Chosen option(s)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateMessagePollVote = ['_' => 'updateMessagePollVote', 'poll_id' => long, 'user_id' => int, 'options' => ['bytes', 'bytes']];
```  


Or, if you're into Lua:

```lua
updateMessagePollVote={_='updateMessagePollVote', poll_id=long, user_id=int, options={'bytes'}}

```


