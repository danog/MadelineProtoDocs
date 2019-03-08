---
title: pollResults
description: Poll results
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pollResults  
[Back to constructors index](index.md)



Poll results

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|min|[Bool](../types/Bool.md) | Optional|Min?|
|results|Array of [PollAnswerVoters](../types/PollAnswerVoters.md) | Optional|Results|
|total\_voters|[int](../types/int.md) | Optional|Total voters|



### Type: [PollResults](../types/PollResults.md)


### Example:

```php
$pollResults = ['_' => 'pollResults', 'min' => Bool, 'results' => [PollAnswerVoters, PollAnswerVoters], 'total_voters' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pollResults", "min": Bool, "results": [PollAnswerVoters], "total_voters": int}
```


Or, if you're into Lua:

```lua
pollResults={_='pollResults', min=Bool, results={PollAnswerVoters}, total_voters=int}

```


