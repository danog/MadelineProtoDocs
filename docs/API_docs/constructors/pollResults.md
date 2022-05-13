---
title: "pollResults"
description: "Results of poll"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pollResults  
[Back to constructors index](/API_docs/constructors/index.html)



Results of poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|min|[Bool](/API_docs/types/Bool.html) | Optional|Similar to [min](https://core.telegram.org/api/min) objects, used for poll constructors that are the same for all users so they don't have option chosen by the current user (you can use [messages.getPollResults](../methods/messages.getPollResults.html) to get the full poll results).|
|results|Array of [PollAnswerVoters](/API_docs/types/PollAnswerVoters.html) | Optional|Poll results|
|total\_voters|[int](/API_docs/types/int.html) | Optional|Total number of people that voted in the poll|
|recent\_voters|Array of [long](/API_docs/types/long.html) | Optional|IDs of the last users that recently voted in the poll|
|solution|[string](/API_docs/types/string.html) | Optional|Explanation of quiz solution|
|solution\_entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|[Message entities for styled text in quiz solution](https://core.telegram.org/api/entities)|



### Type: [PollResults](/API_docs/types/PollResults.html)


### Example:

```
$pollResults = ['_' => 'pollResults', 'min' => Bool, 'results' => [PollAnswerVoters, PollAnswerVoters], 'total_voters' => int, 'recent_voters' => [long, long], 'solution' => 'string', 'solution_entities' => [MessageEntity, MessageEntity]];
```  
