# chatForbidden

> A group to which the user has no access. E.g., because the user was kicked from the group.

[Back to constructors index](/API_docs/constructors/index.html)



A group to which the user has no access. E.g., because the user was kicked from the group.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|User identifier|
|title|[string](/API_docs/types/string.html) | Yes|Group name|



### Type: [Chat](/API_docs/types/Chat.html)


### Example:

```
$chatForbidden = ['_' => 'chatForbidden', 'id' => long, 'title' => 'string'];
```
