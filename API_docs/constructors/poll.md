# poll

> Poll

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
|open\_answers|[Bool](/API_docs/types/Bool.html) | Optional|
|revoting\_disabled|[Bool](/API_docs/types/Bool.html) | Optional|
|shuffle\_answers|[Bool](/API_docs/types/Bool.html) | Optional|
|hide\_results\_until\_close|[Bool](/API_docs/types/Bool.html) | Optional|
|creator|[Bool](/API_docs/types/Bool.html) | Optional|
|subscribers\_only|[Bool](/API_docs/types/Bool.html) | Optional|
|question|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|The question of the poll (only [Premium](https://core.telegram.org/api/premium) users can use [custom emoji entities](https://core.telegram.org/api/custom-emoji) here).|
|answers|Array of [PollAnswer](/API_docs/types/PollAnswer.html) | Yes|The possible answers (2-[poll\_answers\_max](https://core.telegram.org/api/config#poll-answers-max)), vote using [messages.sendVote](../methods/messages.sendVote.html).|
|close\_period|[int](/API_docs/types/int.html) | Optional|Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close\_date.|
|close\_date|[int](/API_docs/types/int.html) | Optional|Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future; can't be used together with close\_period.|
|countries\_iso2|Array of [string](/API_docs/types/string.html) | Optional|
|hash|[long](/API_docs/types/long.html) | Yes|



### Type: [Poll](/API_docs/types/Poll.html)


### Example:

```
$poll = ['_' => 'poll', 'id' => long, 'closed' => Bool, 'public_voters' => Bool, 'multiple_choice' => Bool, 'quiz' => Bool, 'open_answers' => Bool, 'revoting_disabled' => Bool, 'shuffle_answers' => Bool, 'hide_results_until_close' => Bool, 'creator' => Bool, 'subscribers_only' => Bool, 'question' => TextWithEntities, 'answers' => [PollAnswer, PollAnswer], 'close_period' => int, 'close_date' => int, 'countries_iso2' => ['string', 'string'], 'hash' => long];
```
