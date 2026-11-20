# pageListOrderedItemBlocks

> Ordered list of IV blocks

[Back to constructors index](/API_docs/constructors/index.html)



Ordered list of [IV](https://instantview.telegram.org) blocks

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|checkbox|[Bool](/API_docs/types/Bool.html) | Optional|
|checked|[Bool](/API_docs/types/Bool.html) | Optional|
|num|[string](/API_docs/types/string.html) | Optional|Number of element within ordered list|
|blocks|Array of [PageBlock](/API_docs/types/PageBlock.html) | Yes|Item contents|
|value|[int](/API_docs/types/int.html) | Optional|
|type|[string](/API_docs/types/string.html) | Optional|



### Type: [PageListOrderedItem](/API_docs/types/PageListOrderedItem.html)


### Example:

```
$pageListOrderedItemBlocks = ['_' => 'pageListOrderedItemBlocks', 'checkbox' => Bool, 'checked' => Bool, 'num' => 'string', 'blocks' => [PageBlock, PageBlock], 'value' => int, 'type' => 'string'];
```
