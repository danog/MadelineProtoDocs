---
title: "pollResults"
description: "Results of poll"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pollResults  
[Back to constructors index](index.md)



Results of poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|min|[Bool](../types/Bool.md) | Optional|Similar to [min](https://core.telegram.org/api/min) objects, used for poll constructors that are the same for all users so they don't have option chosen by the current user (you can use [messages.getPollResults](../methods/messages.getPollResults.md) to get the full poll results).|
|results|Array of [PollAnswerVoters](../types/PollAnswerVoters.md) | Optional|Poll results|
|total\_voters|[int](../types/int.md) | Optional|Total number of people that voted in the poll|
|recent\_voters|Array of [long](../types/long.md) | Optional|IDs of the last users that recently voted in the poll|
|solution|[string](../types/string.md) | Optional|Explanation of quiz solution|
|solution\_entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|[Message entities for styled text in quiz solution](https://core.telegram.org/api/entities)|



### Type: [PollResults](../types/PollResults.md)


### Example:

```php
$pollResults = ['_' => 'pollResults', 'min' => Bool, 'results' => [PollAnswerVoters, PollAnswerVoters], 'total_voters' => int, 'recent_voters' => [long, long], 'solution' => 'string', 'solution_entities' => [MessageEntity, MessageEntity]];
```  


Or, if you're into Lua:

```lua
pollResults={_='pollResults', min=Bool, results={PollAnswerVoters}, total_voters=int, recent_voters={long}, solution='string', solution_entities={MessageEntity}}

```


