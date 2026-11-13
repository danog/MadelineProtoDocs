# stories.albums

> Story albums ».

[Back to constructors index](/API_docs/constructors/index.html)



[Story albums »](https://core.telegram.org/api/stories#story-albums).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|Hash to pass to [stories.getAlbums](../methods/stories.getAlbums.html) to avoid returning any results if they haven't changed.|
|albums|Array of [StoryAlbum](/API_docs/types/StoryAlbum.html) | Yes|The albums.|



### Type: [stories.Albums](/API_docs/types/stories.Albums.html)


### Example:

```
$stories_albums = ['_' => 'stories.albums', 'hash' => long, 'albums' => [StoryAlbum, StoryAlbum]];
```
