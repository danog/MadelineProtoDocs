# stories.storyReactionsList

> List of peers that reacted to or intercated with a specific story

[Back to constructors index](/API_docs/constructors/index.html)



List of peers that reacted to or intercated with a specific [story](https://core.telegram.org/api/stories)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of reactions matching query|
|reactions|Array of [StoryReaction](/API_docs/types/StoryReaction.html) | Yes|List of peers that reacted to or interacted with a specific story|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|
|next\_offset|[string](/API_docs/types/string.html) | Optional|If set, indicates the next offset to use to load more results by invoking [stories.getStoryReactionsList](../methods/stories.getStoryReactionsList.html).|



### Type: [stories.StoryReactionsList](/API_docs/types/stories.StoryReactionsList.html)


### Example:

```
$stories_storyReactionsList = ['_' => 'stories.storyReactionsList', 'count' => int, 'reactions' => [StoryReaction, StoryReaction], 'chats' => [Chat, Chat], 'users' => [User, User], 'next_offset' => 'string'];
```
