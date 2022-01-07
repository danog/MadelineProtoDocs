---
title: "inputMediaPoll"
description: "A poll"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaPoll  
[Back to constructors index](/API_docs/constructors/index.md)



A poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|poll|[Poll](/API_docs/types/Poll.md) | Yes|The poll to send|
|correct\_answers|Array of [bytes](/API_docs/types/bytes.md) | Optional|Correct answer IDs (for quiz polls)|
|solution|[string](/API_docs/types/string.md) | Optional|Explanation of quiz solution|
|solution\_entities|Array of [MessageEntity](/API_docs/types/MessageEntity.md) | Optional|[Message entities for styled text](https://core.telegram.org/api/entities)|



### Type: [InputMedia](/API_docs/types/InputMedia.md)


### Example:

```php
$inputMediaPoll = ['_' => 'inputMediaPoll', 'poll' => Poll, 'correct_answers' => ['bytes', 'bytes'], 'solution' => 'string', 'solution_entities' => [MessageEntity, MessageEntity]];
```  
