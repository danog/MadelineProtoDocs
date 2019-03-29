---
title: pollAnswerVoters
description: Poll answer voters
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pollAnswerVoters  
[Back to constructors index](index.md)



Poll answer voters

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chosen|[Bool](../types/Bool.md) | Optional|Chosen?|
|option|[bytes](../types/bytes.md) | Yes|Option|
|voters|[int](../types/int.md) | Yes|Voters|



### Type: [PollAnswerVoters](../types/PollAnswerVoters.md)


### Example:

```php
$pollAnswerVoters = ['_' => 'pollAnswerVoters', 'chosen' => Bool, 'option' => 'bytes', 'voters' => int];
```  


Or, if you're into Lua:

```lua
pollAnswerVoters={_='pollAnswerVoters', chosen=Bool, option='bytes', voters=int}

```


