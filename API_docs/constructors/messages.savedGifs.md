# messages.savedGifs

> Saved gifs

[Back to constructors index](/API_docs/constructors/index.html)



Saved gifs

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|gifs|Array of [Document](/API_docs/types/Document.html) | Yes|List of saved gifs|



### Type: [messages.SavedGifs](/API_docs/types/messages.SavedGifs.html)


### Example:

```
$messages_savedGifs = ['_' => 'messages.savedGifs', 'hash' => long, 'gifs' => [Document, Document]];
```
