# channelAdminLogEventActionDeleteTopic

> A forum topic was deleted

[Back to constructors index](/API_docs/constructors/index.html)



A [forum topic](https://core.telegram.org/api/forum#forum-topics) was deleted

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|topic|[ForumTopic](/API_docs/types/ForumTopic.html) | Yes|The [forum topic](https://core.telegram.org/api/forum#forum-topics) that was deleted|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionDeleteTopic = ['_' => 'channelAdminLogEventActionDeleteTopic', 'topic' => ForumTopic];
```
