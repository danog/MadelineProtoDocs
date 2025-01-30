---
title: "updateDeleteQuickReply"
description: "A quick reply shortcut » was deleted. This will not emit updateDeleteQuickReplyMessages updates, even if all the messages in the shortcut are also deleted by this update."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDeleteQuickReply  
[Back to constructors index](/API_docs/constructors/index.html)



A [quick reply shortcut »](https://core.telegram.org/api/business#quick-reply-shortcuts) was deleted. This will **not** emit [updateDeleteQuickReplyMessages](../constructors/updateDeleteQuickReplyMessages.html) updates, even if all the messages in the shortcut are also deleted by this update.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|shortcut\_id|[int](/API_docs/types/int.html) | Yes|ID of the quick reply shortcut that was deleted.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateDeleteQuickReply = ['_' => 'updateDeleteQuickReply', 'shortcut_id' => int];
```  
