# sendMessageTextDraftAction

> sendMessageTextDraftAction attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|can\_stop|[Bool](/API_docs/types/Bool.html) | Optional|
|keep\_on\_stop|[Bool](/API_docs/types/Bool.html) | Optional|
|text|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|



### Type: [SendMessageAction](/API_docs/types/SendMessageAction.html)


### Example:

```
$sendMessageTextDraftAction = ['_' => 'sendMessageTextDraftAction', 'can_stop' => Bool, 'keep_on_stop' => Bool, 'text' => TextWithEntities];
```
