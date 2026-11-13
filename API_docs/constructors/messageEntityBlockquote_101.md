# messageEntityBlockquote

> Message entity representing a block quote.

[Back to constructors index](/API_docs/constructors/index.html)



Message entity representing a block quote.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](/API_docs/types/int.html) | Yes|Offset of message entity within message (in [UTF-16 code units](https://core.telegram.org/api/entities#entity-length))|
|length|[int](/API_docs/types/int.html) | Yes|Length of message entity within message (in [UTF-16 code units](https://core.telegram.org/api/entities#entity-length))|



### Type: [MessageEntity](/API_docs/types/MessageEntity.html)


### Example:

```
$messageEntityBlockquote_101 = ['_' => 'messageEntityBlockquote', 'offset' => int, 'length' => int];
```
