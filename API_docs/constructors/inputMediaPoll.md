# inputMediaPoll

> A poll

[Back to constructors index](/API_docs/constructors/index.html)



A poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|poll|[Poll](/API_docs/types/Poll.html) | Yes|The poll to send|
|correct\_answers|Array of [int](/API_docs/types/int.html) | Optional|Correct answer IDs (for quiz polls)|
|attached\_media|[MessageMedia, Message, Update or InputMedia](/API_docs/types/InputMedia.html) | Optional|
|solution|[string](/API_docs/types/string.html) | Optional|Explanation of quiz solution|
|solution\_entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|[Message entities for styled text](https://core.telegram.org/api/entities)|
|solution\_media|[MessageMedia, Message, Update or InputMedia](/API_docs/types/InputMedia.html) | Optional|



### Type: [InputMedia](/API_docs/types/InputMedia.html)


### Example:

```
$inputMediaPoll = ['_' => 'inputMediaPoll', 'poll' => Poll, 'correct_answers' => [int, int], 'attached_media' => InputMedia, 'solution' => 'string', 'solution_entities' => [MessageEntity, MessageEntity], 'solution_media' => InputMedia];
```
