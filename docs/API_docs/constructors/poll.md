---
title: "poll"
description: "Poll"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: poll  
[Back to constructors index](index.md)



Poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID of the poll|
|closed|[Bool](../types/Bool.md) | Optional|Whether the poll is closed and doesn't accept any more answers|
|public\_voters|[Bool](../types/Bool.md) | Optional|Whether cast votes are publicly visible to all users (non-anonymous poll)|
|multiple\_choice|[Bool](../types/Bool.md) | Optional|Whether multiple options can be chosen as answer|
|quiz|[Bool](../types/Bool.md) | Optional|Whether this is a quiz (with wrong and correct answers, results shown in the return type)|
|question|[string](../types/string.md) | Yes|The question of the poll|
|answers|Array of [PollAnswer](../types/PollAnswer.md) | Yes|The possible answers, vote using [messages.sendVote](../methods/messages.sendVote.md).|
|close\_period|[int](../types/int.md) | Optional|Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close\_date.|
|close\_date|[int](../types/int.md) | Optional|Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future; can't be used together with close\_period.|



### Type: [Poll](../types/Poll.md)


### Example:

```php
$poll = ['_' => 'poll', 'id' => long, 'closed' => Bool, 'public_voters' => Bool, 'multiple_choice' => Bool, 'quiz' => Bool, 'question' => 'string', 'answers' => [PollAnswer, PollAnswer], 'close_period' => int, 'close_date' => int];
```  
