# publicForwardStory

> Contains info about a forward of a story as a repost by a public channel.

[Back to constructors index](/API_docs/constructors/index.html)



Contains info about a forward of a [story](https://core.telegram.org/api/stories) as a repost by a public channel.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|The channel that reposted the story.|
|story|[StoryItem](/API_docs/types/StoryItem.html) | Yes|The reposted story (may be different from the original story).|



### Type: [PublicForward](/API_docs/types/PublicForward.html)


### Example:

```
$publicForwardStory = ['_' => 'publicForwardStory', 'peer' => long, 'story' => StoryItem];
```
