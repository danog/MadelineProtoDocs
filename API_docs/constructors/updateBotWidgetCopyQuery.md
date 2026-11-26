# updateBotWidgetCopyQuery

> updateBotWidgetCopyQuery attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|query\_id|[long](/API_docs/types/long.html) | Yes|
|query\_type|[WidgetQueryType](/API_docs/types/WidgetQueryType.html) | Yes|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|data|[bytes](/API_docs/types/bytes.html) | Yes|
|widget\_id|[long](/API_docs/types/long.html) | Yes|
|wallet\_card|[wallet.Card](/API_docs/constructors/wallet.Card.html) | Optional|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotWidgetCopyQuery = ['_' => 'updateBotWidgetCopyQuery', 'query_id' => long, 'query_type' => WidgetQueryType, 'user_id' => long, 'data' => 'bytes', 'widget_id' => long, 'wallet_card' => wallet.Card];
```
