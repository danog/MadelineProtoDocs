---
title: "pageBlockTable"
description: "Table"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockTable  
[Back to constructors index](/API_docs/constructors/index.html)



Table

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bordered|[Bool](/API_docs/types/Bool.html) | Optional|Does the table have a visible border?|
|striped|[Bool](/API_docs/types/Bool.html) | Optional|Is the table striped?|
|title|[RichText](/API_docs/types/RichText.html) | Yes|Title|
|rows|Array of [PageTableRow](/API_docs/types/PageTableRow.html) | Yes|Table rows|



### Type: [PageBlock](/API_docs/types/PageBlock.html)


### Example:

```
$pageBlockTable = ['_' => 'pageBlockTable', 'bordered' => Bool, 'striped' => Bool, 'title' => RichText, 'rows' => [PageTableRow, PageTableRow]];
```  
