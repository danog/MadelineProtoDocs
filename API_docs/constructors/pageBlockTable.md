# pageBlockTable

> Table

[Back to constructors index](/API_docs/constructors/index.html)



Table

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bordered|[Bool](/API_docs/types/Bool.html) | Optional|Does the table have a visible border?|
|striped|[Bool](/API_docs/types/Bool.html) | Optional|Is the table striped?|
|compact|[Bool](/API_docs/types/Bool.html) | Optional|
|title|[RichText](/API_docs/types/RichText.html) | Yes|Title|
|rows|Array of [PageTableRow](/API_docs/types/PageTableRow.html) | Yes|Table rows|



### Type: [PageBlock](/API_docs/types/PageBlock.html)


### Example:

```
$pageBlockTable = ['_' => 'pageBlockTable', 'bordered' => Bool, 'striped' => Bool, 'compact' => Bool, 'title' => RichText, 'rows' => [PageTableRow, PageTableRow]];
```
