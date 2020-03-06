---
title: messageUserVoteMultiple
description: messageUserVoteMultiple attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageUserVoteMultiple  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[int](../types/int.md) | Yes|
|options|Array of [bytes](../types/bytes.md) | Yes|
|date|[int](../types/int.md) | Yes|



### Type: [MessageUserVote](../types/MessageUserVote.md)


### Example:

```php
$messageUserVoteMultiple = ['_' => 'messageUserVoteMultiple', 'user_id' => int, 'options' => ['bytes', 'bytes'], 'date' => int];
```  


Or, if you're into Lua:

```lua
messageUserVoteMultiple={_='messageUserVoteMultiple', user_id=int, options={'bytes'}, date=int}

```


