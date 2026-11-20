# stories.allStoriesNotModified

> The list of active (or active and hidden) stories has not changed.

[Back to constructors index](/API_docs/constructors/index.html)



The list of active (or active and hidden) [stories](https://core.telegram.org/api/stories#watching-stories) has not changed.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|state|[string](/API_docs/types/string.html) | Yes|State to use to ask for updates|
|stealth\_mode|[StoriesStealthMode](/API_docs/types/StoriesStealthMode.html) | Yes|Current [stealth mode](https://core.telegram.org/api/stories#stealth-mode) information|



### Type: [stories.AllStories](/API_docs/types/stories.AllStories.html)


### Example:

```
$stories_allStoriesNotModified = ['_' => 'stories.allStoriesNotModified', 'state' => 'string', 'stealth_mode' => StoriesStealthMode];
```
