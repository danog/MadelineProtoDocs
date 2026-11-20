# messages.affectedFoundMessages

> Messages found and affected by changes

[Back to constructors index](/API_docs/constructors/index.html)



Messages found and affected by changes

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pts|[int](/API_docs/types/int.html) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.html) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|
|offset|[int](/API_docs/types/int.html) | Yes|If bigger than zero, the request must be repeated to remove more messages|
|messages|Array of [int](/API_docs/types/int.html) | Yes|Affected message IDs|



### Type: [messages.AffectedFoundMessages](/API_docs/types/messages.AffectedFoundMessages.html)


### Example:

```
$messages_affectedFoundMessages = ['_' => 'messages.affectedFoundMessages', 'pts' => int, 'pts_count' => int, 'offset' => int, 'messages' => [int, int]];
```
