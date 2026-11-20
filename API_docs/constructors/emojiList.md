# emojiList

> Represents a list of custom emojis.

[Back to constructors index](/API_docs/constructors/index.html)



Represents a list of [custom emojis](https://core.telegram.org/api/custom-emoji).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|document\_id|Array of [long](/API_docs/types/long.html) | Yes|Custom emoji IDs|



### Type: [EmojiList](/API_docs/types/EmojiList.html)


### Example:

```
$emojiList = ['_' => 'emojiList', 'hash' => long, 'document_id' => [long, long]];
```
