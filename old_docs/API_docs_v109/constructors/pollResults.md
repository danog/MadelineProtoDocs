---
title: pollResults
description: Results of poll
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pollResults  
[Back to constructors index](index.md)



Results of poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|min|[Bool](../types/Bool.md) | Optional|Similar to [min](https://core.telegram.org/api/min) objects, used for poll constructors that are the same for all users so they don't have option chosen by the current user (you can use [messages.getPollResults](../methods/messages.getPollResults.md) to get the full poll results).|
|results|Array of [PollAnswerVoters](../types/PollAnswerVoters.md) | Optional|Results|
|total\_voters|[int](../types/int.md) | Optional|Total number of people that voted in the poll|
|recent\_voters|Array of [int](../types/int.md) | Optional||



### Type: [PollResults](../types/PollResults.md)


### Example:

```php
$pollResults = ['_' => 'pollResults', 'min' => Bool, 'results' => [PollAnswerVoters, PollAnswerVoters], 'total_voters' => int, 'recent_voters' => [int, int]];
```  


Or, if you're into Lua:

```lua
pollResults={_='pollResults', min=Bool, results={PollAnswerVoters}, total_voters=int, recent_voters={int}}

```


