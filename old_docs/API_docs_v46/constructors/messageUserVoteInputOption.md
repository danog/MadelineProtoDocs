---
title: messageUserVoteInputOption
description: How a user voted in a poll (reduced constructor, returned if an `option` was provided to [messages.getPollVotes](../methods/messages.getPollVotes.md))
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageUserVoteInputOption  
[Back to constructors index](index.md)



How a user voted in a poll (reduced constructor, returned if an `option` was provided to [messages.getPollVotes](../methods/messages.getPollVotes.md))

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|The user that voted for the queried `option`|
|date|[int](../types/int.md) | Yes|When did the user cast the vote|



### Type: [MessageUserVote](../types/MessageUserVote.md)


### Example:

```php
$messageUserVoteInputOption = ['_' => 'messageUserVoteInputOption', 'user_id' => int, 'date' => int];
```  


Or, if you're into Lua:

```lua
messageUserVoteInputOption={_='messageUserVoteInputOption', user_id=int, date=int}

```


