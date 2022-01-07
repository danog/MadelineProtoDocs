---
title: "pollAnswerVoters"
description: "A poll answer, and how users voted on it"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pollAnswerVoters  
[Back to constructors index](/API_docs/constructors/index.md)



A poll answer, and how users voted on it

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chosen|[Bool](/API_docs/types/Bool.md) | Optional|Whether we have chosen this answer|
|correct|[Bool](/API_docs/types/Bool.md) | Optional|For quizes, whether the option we have chosen is correct|
|option|[bytes](/API_docs/types/bytes.md) | Yes|The param that has to be passed to [messages.sendVote](../methods/messages.sendVote.md).|
|voters|[int](/API_docs/types/int.md) | Yes|How many users voted for this option|



### Type: [PollAnswerVoters](/API_docs/types/PollAnswerVoters.md)


### Example:

```php
$pollAnswerVoters = ['_' => 'pollAnswerVoters', 'chosen' => Bool, 'correct' => Bool, 'option' => 'bytes', 'voters' => int];
```  
