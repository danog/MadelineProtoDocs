---
title: pageBlockTable
description: Page block table
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockTable  
[Back to constructors index](index.md)



Page block table

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bordered|[Bool](../types/Bool.md) | Optional|Bordered?|
|striped|[Bool](../types/Bool.md) | Optional|Striped?|
|title|[RichText](../types/RichText.md) | Yes|Title|
|rows|Array of [PageTableRow](../types/PageTableRow.md) | Yes|Rows|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockTable = ['_' => 'pageBlockTable', 'bordered' => Bool, 'striped' => Bool, 'title' => RichText, 'rows' => [PageTableRow, PageTableRow]];
```  


Or, if you're into Lua:

```lua
pageBlockTable={_='pageBlockTable', bordered=Bool, striped=Bool, title=RichText, rows={PageTableRow}}

```


