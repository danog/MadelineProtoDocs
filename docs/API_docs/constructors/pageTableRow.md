---
title: pageTableRow
description: Page table row
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageTableRow  
[Back to constructors index](index.md)



Page table row

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|cells|Array of [PageTableCell](../types/PageTableCell.md) | Yes|Cells|



### Type: [PageTableRow](../types/PageTableRow.md)


### Example:

```php
$pageTableRow = ['_' => 'pageTableRow', 'cells' => [PageTableCell, PageTableCell]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageTableRow", "cells": [PageTableCell]}
```


Or, if you're into Lua:

```lua
pageTableRow={_='pageTableRow', cells={PageTableCell}}

```


