# prepaidGiveaway

> Contains info about a prepaid giveaway ».

[Back to constructors index](/API_docs/constructors/index.html)



Contains info about a [prepaid giveaway »](https://core.telegram.org/api/giveaways).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Prepaid giveaway ID.|
|months|[int](/API_docs/types/int.html) | Yes|Duration in months of each gifted [Telegram Premium](https://core.telegram.org/api/premium) subscription.|
|quantity|[int](/API_docs/types/int.html) | Yes|Number of given away [Telegram Premium](https://core.telegram.org/api/premium) subscriptions.|
|date|[int](/API_docs/types/int.html) | Yes|Payment date.|



### Type: [PrepaidGiveaway](/API_docs/types/PrepaidGiveaway.html)


### Example:

```
$prepaidGiveaway = ['_' => 'prepaidGiveaway', 'id' => long, 'months' => int, 'quantity' => int, 'date' => int];
```
