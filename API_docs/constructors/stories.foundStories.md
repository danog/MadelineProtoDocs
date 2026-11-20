# stories.foundStories

> Stories found using global story search ».

[Back to constructors index](/API_docs/constructors/index.html)



Stories found using [global story search »](https://core.telegram.org/api/stories#searching-stories).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of results found for the query.|
|stories|Array of [FoundStory](/API_docs/types/FoundStory.html) | Yes|Matching stories.|
|next\_offset|[string](/API_docs/types/string.html) | Optional|Offset used to fetch the next page, if not set this is the final page.|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [stories.FoundStories](/API_docs/types/stories.FoundStories.html)


### Example:

```
$stories_foundStories = ['_' => 'stories.foundStories', 'count' => int, 'stories' => [FoundStory, FoundStory], 'next_offset' => 'string', 'chats' => [Chat, Chat], 'users' => [User, User]];
```
