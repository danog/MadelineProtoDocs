---
title: "pageBlockTable"
description: "Table"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockTable  
[Back to constructors index](index.md)



Table

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bordered|[Bool](../types/Bool.md) | Optional|Does the table have a visible border?|
|striped|[Bool](../types/Bool.md) | Optional|Is the table striped?|
|title|[RichText](../types/RichText.md) | Yes|Title|
|rows|Array of [PageTableRow](../types/PageTableRow.md) | Yes|Table rows|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockTable = ['_' => 'pageBlockTable', 'bordered' => Bool, 'striped' => Bool, 'title' => RichText, 'rows' => [PageTableRow, PageTableRow]];
```  
