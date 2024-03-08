---
title: "updateSavedDialogPinned"
description: "A saved message dialog was pinned/unpinned"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateSavedDialogPinned  
[Back to constructors index](/API_docs/constructors/index.html)



A [saved message dialog](https://core.telegram.org/api/saved-messages) was pinned/unpinned

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](/API_docs/types/Bool.html) | Optional|Whether the dialog was pinned|
|peer|[DialogPeer](/API_docs/types/DialogPeer.html) | Yes|The dialog|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateSavedDialogPinned = ['_' => 'updateSavedDialogPinned', 'pinned' => Bool, 'peer' => DialogPeer];
```  
