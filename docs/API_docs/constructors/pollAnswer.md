---
title: "pollAnswer"
description: "A possible answer of a poll"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pollAnswer  
[Back to constructors index](/API_docs/constructors/index.html)



A possible answer of a poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](/API_docs/types/string.html) | Yes|Textual representation of the answer|
|option|[bytes](/API_docs/types/bytes.html) | Yes|The param that has to be passed to [messages.sendVote](../methods/messages.sendVote.html).|



### Type: [PollAnswer](/API_docs/types/PollAnswer.html)


### Example:

```
$pollAnswer = ['_' => 'pollAnswer', 'text' => 'string', 'option' => 'bytes'];
```  
