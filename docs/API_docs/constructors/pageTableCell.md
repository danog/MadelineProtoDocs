---
title: "pageTableCell"
description: "Table cell"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageTableCell  
[Back to constructors index](index.md)



Table cell

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|header|[Bool](../types/Bool.md) | Optional|Is this element part of the column header|
|align\_center|[Bool](../types/Bool.md) | Optional|Horizontally centered block|
|align\_right|[Bool](../types/Bool.md) | Optional|Right-aligned block|
|valign\_middle|[Bool](../types/Bool.md) | Optional|Vertically centered block|
|valign\_bottom|[Bool](../types/Bool.md) | Optional|Block vertically-alligned to the bottom|
|text|[RichText](../types/RichText.md) | Optional|Content|
|colspan|[int](../types/int.md) | Optional|For how many columns should this cell extend|
|rowspan|[int](../types/int.md) | Optional|For how many rows should this cell extend|



### Type: [PageTableCell](../types/PageTableCell.md)


### Example:

```php
$pageTableCell = ['_' => 'pageTableCell', 'header' => Bool, 'align_center' => Bool, 'align_right' => Bool, 'valign_middle' => Bool, 'valign_bottom' => Bool, 'text' => RichText, 'colspan' => int, 'rowspan' => int];
```  


Or, if you're into Lua:

```lua
pageTableCell={_='pageTableCell', header=Bool, align_center=Bool, align_right=Bool, valign_middle=Bool, valign_bottom=Bool, text=RichText, colspan=int, rowspan=int}

```


