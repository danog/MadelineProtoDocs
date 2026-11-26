# pageBlockBlockquoteBlocks

> pageBlockBlockquoteBlocks attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|collapsed|[Bool](/API_docs/types/Bool.html) | Optional|
|blocks|Array of [PageBlock](/API_docs/types/PageBlock.html) | Yes|
|caption|[RichText](/API_docs/types/RichText.html) | Yes|



### Type: [PageBlock](/API_docs/types/PageBlock.html)


### Example:

```
$pageBlockBlockquoteBlocks = ['_' => 'pageBlockBlockquoteBlocks', 'collapsed' => Bool, 'blocks' => [PageBlock, PageBlock], 'caption' => RichText];
```
