# messageActionChatCreate

> Group created

[Back to constructors index](/API_docs/constructors/index.html)



Group created

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](/API_docs/types/string.html) | Yes|Group name|
|users|Array of [long](/API_docs/types/long.html) | Yes|List of group members|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionChatCreate = ['_' => 'messageActionChatCreate', 'title' => 'string', 'users' => [long, long]];
```
