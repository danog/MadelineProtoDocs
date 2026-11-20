# updateStory

> A new story was posted.

[Back to constructors index](/API_docs/constructors/index.html)



A new story was posted.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|ID of the poster.|
|story|[StoryItem](/API_docs/types/StoryItem.html) | Yes|The story that was posted.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateStory = ['_' => 'updateStory', 'peer' => long, 'story' => StoryItem];
```
