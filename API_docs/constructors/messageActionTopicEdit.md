# messageActionTopicEdit

> Forum topic information was edited.

[Back to constructors index](/API_docs/constructors/index.html)



[Forum topic](https://core.telegram.org/api/forum#forum-topics) information was edited.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](/API_docs/types/string.html) | Optional|New topic title.|
|icon\_emoji\_id|[long](/API_docs/types/long.html) | Optional|ID of the new [custom emoji](https://core.telegram.org/api/custom-emoji) used as topic icon, or if it was removed.|
|closed|[Bool](/API_docs/types/Bool.html) | Optional|Whether the topic was opened or closed.|
|hidden|[Bool](/API_docs/types/Bool.html) | Optional|Whether the topic was hidden or unhidden (only valid for the "General" topic, `id=1`).|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionTopicEdit = ['_' => 'messageActionTopicEdit', 'title' => 'string', 'icon_emoji_id' => long, 'closed' => Bool, 'hidden' => Bool];
```
