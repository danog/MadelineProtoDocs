# starGiftAttributeCounter

> Indicates the total number of gifts that have the specified attribute.

[Back to constructors index](/API_docs/constructors/index.html)



Indicates the total number of gifts that have the specified attribute.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|attribute|[StarGiftAttributeId](/API_docs/types/StarGiftAttributeId.html) | Yes|The attribute (just the ID, without the attribute itself).|
|count|[int](/API_docs/types/int.html) | Yes|Total number of gifts with this attribute.|



### Type: [StarGiftAttributeCounter](/API_docs/types/StarGiftAttributeCounter.html)


### Example:

```
$starGiftAttributeCounter = ['_' => 'starGiftAttributeCounter', 'attribute' => StarGiftAttributeId, 'count' => int];
```
