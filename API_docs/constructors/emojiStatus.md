# emojiStatus

> An emoji status

[Back to constructors index](/API_docs/constructors/index.html)



An [emoji status](https://core.telegram.org/api/emoji-status)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|document\_id|[long](/API_docs/types/long.html) | Yes|[Custom emoji document ID](https://core.telegram.org/api/custom-emoji)|
|until|[int](/API_docs/types/int.html) | Optional|If set, the emoji status will be active until the specified unixtime.|



### Type: [EmojiStatus](/API_docs/types/EmojiStatus.html)


### Example:

```
$emojiStatus = ['_' => 'emojiStatus', 'document_id' => long, 'until' => int];
```
