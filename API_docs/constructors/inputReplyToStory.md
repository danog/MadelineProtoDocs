# inputReplyToStory

> Reply to a story.

[Back to constructors index](/API_docs/constructors/index.html)



Reply to a story.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|Sender of the story|
|story\_id|[int](/API_docs/types/int.html) | Yes|ID of the story to reply to.|



### Type: [InputReplyTo](/API_docs/types/InputReplyTo.html)


### Example:

```
$inputReplyToStory = ['_' => 'inputReplyToStory', 'peer' => InputPeer, 'story_id' => int];
```
