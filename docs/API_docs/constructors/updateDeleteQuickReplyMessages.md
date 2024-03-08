---
title: "updateDeleteQuickReplyMessages"
description: "updateDeleteQuickReplyMessages attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDeleteQuickReplyMessages  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|shortcut\_id|[int](/API_docs/types/int.html) | Yes|
|messages|Array of [int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateDeleteQuickReplyMessages = ['_' => 'updateDeleteQuickReplyMessages', 'shortcut_id' => int, 'messages' => [int, int]];
```  
