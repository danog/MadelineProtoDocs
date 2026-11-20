# updateChannelMessageForwards

> The forward counter of a message in a channel has changed

[Back to constructors index](/API_docs/constructors/index.html)



The forward counter of a message in a channel has changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|Channel ID|
|id|[int](/API_docs/types/int.html) | Yes|ID of the message|
|forwards|[int](/API_docs/types/int.html) | Yes|New forward counter|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChannelMessageForwards = ['_' => 'updateChannelMessageForwards', 'channel_id' => long, 'id' => int, 'forwards' => int];
```
