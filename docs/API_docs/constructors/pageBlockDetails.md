---
title: "pageBlockDetails"
description: "A collapsible details block"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockDetails  
[Back to constructors index](/API_docs/constructors/index.html)



A collapsible details block

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|open|[Bool](/API_docs/types/Bool.html) | Optional|Whether the block is open by default|
|blocks|Array of [PageBlock](/API_docs/types/PageBlock.html) | Yes|Block contents|
|title|[RichText](/API_docs/types/RichText.html) | Yes|Always visible heading for the block|



### Type: [PageBlock](/API_docs/types/PageBlock.html)


### Example:

```
$pageBlockDetails = ['_' => 'pageBlockDetails', 'open' => Bool, 'blocks' => [PageBlock, PageBlock], 'title' => RichText];
```  
