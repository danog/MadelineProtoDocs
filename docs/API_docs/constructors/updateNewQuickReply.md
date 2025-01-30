---
title: "updateNewQuickReply"
description: "A new quick reply shortcut » was created."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewQuickReply  
[Back to constructors index](/API_docs/constructors/index.html)



A new [quick reply shortcut »](https://core.telegram.org/api/business#quick-reply-shortcuts) was created.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|quick\_reply|[QuickReply](/API_docs/types/QuickReply.html) | Yes|Quick reply shortcut.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateNewQuickReply = ['_' => 'updateNewQuickReply', 'quick_reply' => QuickReply];
```  
