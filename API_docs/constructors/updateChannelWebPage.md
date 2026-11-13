# updateChannelWebPage

> A webpage preview of a link in a channel/supergroup message was generated

[Back to constructors index](/API_docs/constructors/index.html)



A webpage preview of a link in a [channel/supergroup](https://core.telegram.org/api/channel) message was generated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|[Channel/supergroup](https://core.telegram.org/api/channel) ID|
|webpage|[WebPage](/API_docs/types/WebPage.html) | Optional|Generated webpage preview|
|pts|[int](/API_docs/types/int.html) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.html) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChannelWebPage = ['_' => 'updateChannelWebPage', 'channel_id' => long, 'webpage' => WebPage, 'pts' => int, 'pts_count' => int];
```
