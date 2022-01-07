---
title: "pageBlockDetails"
description: "A collapsible details block"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockDetails  
[Back to constructors index](/API_docs/constructors/index.md)



A collapsible details block

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|open|[Bool](/API_docs/types/Bool.md) | Optional|Whether the block is open by default|
|blocks|Array of [PageBlock](/API_docs/types/PageBlock.md) | Yes|Block contents|
|title|[RichText](/API_docs/types/RichText.md) | Yes|Always visible heading for the block|



### Type: [PageBlock](/API_docs/types/PageBlock.md)


### Example:

```php
$pageBlockDetails = ['_' => 'pageBlockDetails', 'open' => Bool, 'blocks' => [PageBlock, PageBlock], 'title' => RichText];
```  
