---
title: "pollAnswer"
description: "A possible answer of a poll"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pollAnswer  
[Back to constructors index](/API_docs/constructors/index.md)



A possible answer of a poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](/API_docs/types/string.md) | Yes|Textual representation of the answer|
|option|[bytes](/API_docs/types/bytes.md) | Yes|The param that has to be passed to [messages.sendVote](../methods/messages.sendVote.md).|



### Type: [PollAnswer](/API_docs/types/PollAnswer.md)


### Example:

```php
$pollAnswer = ['_' => 'pollAnswer', 'text' => 'string', 'option' => 'bytes'];
```  
