# pollAnswerVoters

> A poll answer, and how users voted on it

[Back to constructors index](/API_docs/constructors/index.html)



A poll answer, and how users voted on it

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chosen|[Bool](/API_docs/types/Bool.html) | Optional|Whether we have chosen this answer|
|correct|[Bool](/API_docs/types/Bool.html) | Optional|For quizzes, whether the option we have chosen is correct|
|option|[bytes](/API_docs/types/bytes.html) | Yes|The param that has to be passed to [messages.sendVote](../methods/messages.sendVote.html).|
|voters|[int](/API_docs/types/int.html) | Optional|How many users voted for this option|
|recent\_voters|Array of [Peer](/API_docs/types/Peer.html) | Optional|



### Type: [PollAnswerVoters](/API_docs/types/PollAnswerVoters.html)


### Example:

```
$pollAnswerVoters = ['_' => 'pollAnswerVoters', 'chosen' => Bool, 'correct' => Bool, 'option' => 'bytes', 'voters' => int, 'recent_voters' => [Peer, Peer]];
```
