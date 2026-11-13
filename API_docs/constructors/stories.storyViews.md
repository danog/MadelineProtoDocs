# stories.storyViews

> Reaction and view counters for a list of stories

[Back to constructors index](/API_docs/constructors/index.html)



Reaction and view counters for a list of [stories](https://core.telegram.org/api/stories)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|views|Array of [StoryViews](/API_docs/types/StoryViews.html) | Yes|View date and reaction information of multiple stories|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [stories.StoryViews](/API_docs/types/stories.StoryViews.html)


### Example:

```
$stories_storyViews = ['_' => 'stories.storyViews', 'views' => [StoryViews, StoryViews], 'users' => [User, User]];
```
