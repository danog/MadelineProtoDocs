---
title: "quickReply"
description: "A quick reply shortcut."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: quickReply  
[Back to constructors index](/API_docs/constructors/index.html)



A [quick reply shortcut](https://core.telegram.org/api/business#quick-reply-shortcuts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|shortcut\_id|[int](/API_docs/types/int.html) | Yes|Unique shortcut ID.|
|shortcut|[string](/API_docs/types/string.html) | Yes|Shortcut name.|
|top\_message|[int](/API_docs/types/int.html) | Yes|ID of the last message in the shortcut.|
|count|[int](/API_docs/types/int.html) | Yes|Total number of messages in the shortcut.|



### Type: [QuickReply](/API_docs/types/QuickReply.html)


### Example:

```
$quickReply = ['_' => 'quickReply', 'shortcut_id' => int, 'shortcut' => 'string', 'top_message' => int, 'count' => int];
```  
