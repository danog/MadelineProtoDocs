---
title: "pageBlockButtonRow"
description: "pageBlockButtonRow attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockButtonRow  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|align\_left|[Bool](/API_docs/types/Bool.html) | Optional|
|align\_center|[Bool](/API_docs/types/Bool.html) | Optional|
|align\_right|[Bool](/API_docs/types/Bool.html) | Optional|
|buttons|Array of [PageButton](/API_docs/types/PageButton.html) | Yes|



### Type: [PageBlock](/API_docs/types/PageBlock.html)


### Example:

```
$pageBlockButtonRow = ['_' => 'pageBlockButtonRow', 'align_left' => Bool, 'align_center' => Bool, 'align_right' => Bool, 'buttons' => [PageButton, PageButton]];
```  
