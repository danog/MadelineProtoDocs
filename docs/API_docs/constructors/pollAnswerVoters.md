---
title: "pollAnswerVoters"
description: "A poll answer, and how users voted on it"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pollAnswerVoters  
[Back to constructors index](/API_docs/constructors/index.html)



A poll answer, and how users voted on it

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chosen|[Bool](/API_docs/types/Bool.html) | Optional|Whether we have chosen this answer|
|correct|[Bool](/API_docs/types/Bool.html) | Optional|For quizzes, whether the option we have chosen is correct|
|option|[bytes](/API_docs/types/bytes.html) | Yes|The param that has to be passed to [messages.sendVote](../methods/messages.sendVote.html).|
|voters|[int](/API_docs/types/int.html) | Yes|How many users voted for this option|



### Type: [PollAnswerVoters](/API_docs/types/PollAnswerVoters.html)


### Example:

```
$pollAnswerVoters = ['_' => 'pollAnswerVoters', 'chosen' => Bool, 'correct' => Bool, 'option' => 'bytes', 'voters' => int];
```  
