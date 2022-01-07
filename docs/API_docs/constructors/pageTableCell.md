---
title: "pageTableCell"
description: "Table cell"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageTableCell  
[Back to constructors index](/API_docs/constructors/index.md)



Table cell

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|header|[Bool](/API_docs/types/Bool.md) | Optional|Is this element part of the column header|
|align\_center|[Bool](/API_docs/types/Bool.md) | Optional|Horizontally centered block|
|align\_right|[Bool](/API_docs/types/Bool.md) | Optional|Right-aligned block|
|valign\_middle|[Bool](/API_docs/types/Bool.md) | Optional|Vertically centered block|
|valign\_bottom|[Bool](/API_docs/types/Bool.md) | Optional|Block vertically-alligned to the bottom|
|text|[RichText](/API_docs/types/RichText.md) | Optional|Content|
|colspan|[int](/API_docs/types/int.md) | Optional|For how many columns should this cell extend|
|rowspan|[int](/API_docs/types/int.md) | Optional|For how many rows should this cell extend|



### Type: [PageTableCell](/API_docs/types/PageTableCell.md)


### Example:

```php
$pageTableCell = ['_' => 'pageTableCell', 'header' => Bool, 'align_center' => Bool, 'align_right' => Bool, 'valign_middle' => Bool, 'valign_bottom' => Bool, 'text' => RichText, 'colspan' => int, 'rowspan' => int];
```  
