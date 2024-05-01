---
title: "updateDialogUnreadMark"
description: "The manual unread mark of a chat was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDialogUnreadMark  
[Back to constructors index](/API_docs/constructors/index.html)



The manual unread mark of a chat was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|unread|[Bool](/API_docs/types/Bool.html) | Optional|Was the chat marked or unmarked as read|
|peer|[DialogPeer](/API_docs/types/DialogPeer.html) | Yes|The dialog|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateDialogUnreadMark = ['_' => 'updateDialogUnreadMark', 'unread' => Bool, 'peer' => DialogPeer];
```  
