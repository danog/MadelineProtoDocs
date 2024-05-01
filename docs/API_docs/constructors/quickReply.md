---
title: "quickReply"
description: "quickReply attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: quickReply  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|shortcut\_id|[int](/API_docs/types/int.html) | Yes|
|shortcut|[string](/API_docs/types/string.html) | Yes|
|top\_message|[int](/API_docs/types/int.html) | Yes|
|count|[int](/API_docs/types/int.html) | Yes|



### Type: [QuickReply](/API_docs/types/QuickReply.html)


### Example:

```
$quickReply = ['_' => 'quickReply', 'shortcut_id' => int, 'shortcut' => 'string', 'top_message' => int, 'count' => int];
```  
