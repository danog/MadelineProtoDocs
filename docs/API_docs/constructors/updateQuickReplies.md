---
title: "updateQuickReplies"
description: "Info about or the order of quick reply shortcuts » was changed."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateQuickReplies  
[Back to constructors index](/API_docs/constructors/index.html)



Info about or the order of [quick reply shortcuts »](https://core.telegram.org/api/business#quick-reply-shortcuts) was changed.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|quick\_replies|Array of [QuickReply](/API_docs/types/QuickReply.html) | Yes|New quick reply shortcut order and information.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateQuickReplies = ['_' => 'updateQuickReplies', 'quick_replies' => [QuickReply, QuickReply]];
```  
