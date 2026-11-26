# updateInlineBotWidgetQuery

> updateInlineBotWidgetQuery attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|query\_id|[long](/API_docs/types/long.html) | Yes|
|query\_type|[WidgetQueryType](/API_docs/types/WidgetQueryType.html) | Yes|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|inline\_message\_id|[InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.html) | Yes|
|chat\_instance|[long](/API_docs/types/long.html) | Yes|
|chat\_type|[string](/API_docs/types/string.html) | Yes|
|data|[bytes](/API_docs/types/bytes.html) | Yes|
|widget\_id|[long](/API_docs/types/long.html) | Optional|
|wallet\_card|[wallet.Card](/API_docs/constructors/wallet.Card.html) | Optional|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateInlineBotWidgetQuery = ['_' => 'updateInlineBotWidgetQuery', 'query_id' => long, 'query_type' => WidgetQueryType, 'user_id' => long, 'inline_message_id' => InputBotInlineMessageID, 'chat_instance' => long, 'chat_type' => 'string', 'data' => 'bytes', 'widget_id' => long, 'wallet_card' => wallet.Card];
```
