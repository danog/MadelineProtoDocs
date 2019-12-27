---
title: pollAnswerVoters
description: A poll answer, and how users voted on it
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pollAnswerVoters  
[Back to constructors index](index.md)



A poll answer, and how users voted on it

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chosen|[Bool](../types/Bool.md) | Optional|Whether we have chosen this answer|
|option|[bytes](../types/bytes.md) | Yes|The param that has to be passed to [messages.sendVote](../methods/messages.sendVote.md).|
|voters|[int](../types/int.md) | Yes|How many users voted for this option|



### Type: [PollAnswerVoters](../types/PollAnswerVoters.md)


### Example:

```php
$pollAnswerVoters = ['_' => 'pollAnswerVoters', 'chosen' => Bool, 'option' => 'bytes', 'voters' => int];
```  


Or, if you're into Lua:

```lua
pollAnswerVoters={_='pollAnswerVoters', chosen=Bool, option='bytes', voters=int}

```


