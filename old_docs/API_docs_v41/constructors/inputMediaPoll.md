---
title: inputMediaPoll
description: A poll
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaPoll  
[Back to constructors index](index.md)



A poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|poll|[Poll](../types/Poll.md) | Yes|The poll to send|
|correct\_answers|Array of [bytes](../types/bytes.md) | Optional|Correct answer IDs (for quiz polls)|
|solution|[string](../types/string.md) | Optional|Explanation of quiz solution|
|solution\_entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|[Message entities for styled text](https://core.telegram.org/api/entities)|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaPoll = ['_' => 'inputMediaPoll', 'poll' => Poll, 'correct_answers' => ['bytes', 'bytes'], 'solution' => 'string', 'solution_entities' => [MessageEntity, MessageEntity]];
```  


Or, if you're into Lua:

```lua
inputMediaPoll={_='inputMediaPoll', poll=Poll, correct_answers={'bytes'}, solution='string', solution_entities={MessageEntity}}

```


