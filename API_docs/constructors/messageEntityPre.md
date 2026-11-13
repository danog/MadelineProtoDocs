# messageEntityPre

> Message entity representing a preformatted codeblock, allowing the user to specify a programming language for the codeblock.

[Back to constructors index](/API_docs/constructors/index.html)



Message entity representing a preformatted `codeblock`, allowing the user to specify a programming language for the codeblock.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](/API_docs/types/int.html) | Yes|Offset of message entity within message (in [UTF-16 code units](https://core.telegram.org/api/entities#entity-length))|
|length|[int](/API_docs/types/int.html) | Yes|Length of message entity within message (in [UTF-16 code units](https://core.telegram.org/api/entities#entity-length))|
|language|[string](/API_docs/types/string.html) | Yes|Programming language of the code|



### Type: [MessageEntity](/API_docs/types/MessageEntity.html)


### Example:

```
$messageEntityPre = ['_' => 'messageEntityPre', 'offset' => int, 'length' => int, 'language' => 'string'];
```
