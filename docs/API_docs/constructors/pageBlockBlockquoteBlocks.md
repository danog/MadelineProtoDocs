---
title: "pageBlockBlockquoteBlocks"
description: "pageBlockBlockquoteBlocks attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockBlockquoteBlocks  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|collapsed|[Bool](/API_docs/types/Bool.html) | Optional|
|blocks|Array of [PageBlock](/API_docs/types/PageBlock.html) | Yes|
|caption|[RichText](/API_docs/types/RichText.html) | Yes|



### Type: [PageBlock](/API_docs/types/PageBlock.html)


### Example:

```
$pageBlockBlockquoteBlocks = ['_' => 'pageBlockBlockquoteBlocks', 'collapsed' => Bool, 'blocks' => [PageBlock, PageBlock], 'caption' => RichText];
```  
