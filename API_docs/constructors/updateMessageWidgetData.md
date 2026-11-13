# updateMessageWidgetData

> updateMessageWidgetData attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[long](/API_docs/types/long.html) | Yes|
|msg\_id|[int](/API_docs/types/int.html) | Yes|
|public\_data|[string](/API_docs/types/string.html) | Optional|
|public\_data\_hash|[long](/API_docs/types/long.html) | Optional|
|chat\_data|[string](/API_docs/types/string.html) | Optional|
|pts|[int](/API_docs/types/int.html) | Yes|
|pts\_count|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateMessageWidgetData = ['_' => 'updateMessageWidgetData', 'peer' => long, 'msg_id' => int, 'public_data' => 'string', 'public_data_hash' => long, 'chat_data' => 'string', 'pts' => int, 'pts_count' => int];
```
