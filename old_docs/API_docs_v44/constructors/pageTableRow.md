---
title: pageTableRow
description: Table row
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageTableRow  
[Back to constructors index](index.md)



Table row

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|cells|Array of [PageTableCell](../types/PageTableCell.md) | Yes|Table cells|



### Type: [PageTableRow](../types/PageTableRow.md)


### Example:

```php
$pageTableRow = ['_' => 'pageTableRow', 'cells' => [PageTableCell, PageTableCell]];
```  


Or, if you're into Lua:

```lua
pageTableRow={_='pageTableRow', cells={PageTableCell}}

```


