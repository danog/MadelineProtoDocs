# channelAdminLogEventActionChangeEmojiStatus

> The emoji status was changed

[Back to constructors index](/API_docs/constructors/index.html)



The [emoji status](https://core.telegram.org/api/emoji-status) was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[EmojiStatus](/API_docs/types/EmojiStatus.html) | Optional|Previous emoji status|
|new\_value|[EmojiStatus](/API_docs/types/EmojiStatus.html) | Optional|New emoji status|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionChangeEmojiStatus = ['_' => 'channelAdminLogEventActionChangeEmojiStatus', 'prev_value' => EmojiStatus, 'new_value' => EmojiStatus];
```
