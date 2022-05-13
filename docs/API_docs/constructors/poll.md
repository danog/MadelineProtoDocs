---
title: "poll"
description: "Poll"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: poll  
[Back to constructors index](/API_docs/constructors/index.html)



Poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|ID of the poll|
|closed|[Bool](/API_docs/types/Bool.html) | Optional|Whether the poll is closed and doesn't accept any more answers|
|public\_voters|[Bool](/API_docs/types/Bool.html) | Optional|Whether cast votes are publicly visible to all users (non-anonymous poll)|
|multiple\_choice|[Bool](/API_docs/types/Bool.html) | Optional|Whether multiple options can be chosen as answer|
|quiz|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is a quiz (with wrong and correct answers, results shown in the return type)|
|question|[string](/API_docs/types/string.html) | Yes|The question of the poll|
|answers|Array of [PollAnswer](/API_docs/types/PollAnswer.html) | Yes|The possible answers, vote using [messages.sendVote](../methods/messages.sendVote.html).|
|close\_period|[int](/API_docs/types/int.html) | Optional|Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close\_date.|
|close\_date|[int](/API_docs/types/int.html) | Optional|Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future; can't be used together with close\_period.|



### Type: [Poll](/API_docs/types/Poll.html)


### Example:

```
$poll = ['_' => 'poll', 'id' => long, 'closed' => Bool, 'public_voters' => Bool, 'multiple_choice' => Bool, 'quiz' => Bool, 'question' => 'string', 'answers' => [PollAnswer, PollAnswer], 'close_period' => int, 'close_date' => int];
```  
