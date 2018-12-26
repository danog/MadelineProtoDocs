---
title: pageTableCell
description: Page table cell
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageTableCell  
[Back to constructors index](index.md)



Page table cell

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|header|[Bool](../types/Bool.md) | Optional|Header?|
|align\_center|[Bool](../types/Bool.md) | Optional|Align center?|
|align\_right|[Bool](../types/Bool.md) | Optional|Align right?|
|valign\_middle|[Bool](../types/Bool.md) | Optional|Valign middle?|
|valign\_bottom|[Bool](../types/Bool.md) | Optional|Valign bottom?|
|text|[RichText](../types/RichText.md) | Optional|Text|
|colspan|[int](../types/int.md) | Optional|Colspan|
|rowspan|[int](../types/int.md) | Optional|Rowspan|



### Type: [PageTableCell](../types/PageTableCell.md)


### Example:

```php
$pageTableCell = ['_' => 'pageTableCell', 'header' => Bool, 'align_center' => Bool, 'align_right' => Bool, 'valign_middle' => Bool, 'valign_bottom' => Bool, 'text' => RichText, 'colspan' => int, 'rowspan' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageTableCell", "header": Bool, "align_center": Bool, "align_right": Bool, "valign_middle": Bool, "valign_bottom": Bool, "text": RichText, "colspan": int, "rowspan": int}
```


Or, if you're into Lua:

```lua
pageTableCell={_='pageTableCell', header=Bool, align_center=Bool, align_right=Bool, valign_middle=Bool, valign_bottom=Bool, text=RichText, colspan=int, rowspan=int}

```


