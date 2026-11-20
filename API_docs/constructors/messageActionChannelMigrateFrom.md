# messageActionChannelMigrateFrom

> Indicates the channel was migrated from the specified chat

[Back to constructors index](/API_docs/constructors/index.html)



Indicates the channel was [migrated](https://core.telegram.org/api/channel) from the specified chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](/API_docs/types/string.html) | Yes|The old chat title|
|chat\_id|[long](/API_docs/types/long.html) | Yes|The old chat ID|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionChannelMigrateFrom = ['_' => 'messageActionChannelMigrateFrom', 'title' => 'string', 'chat_id' => long];
```
