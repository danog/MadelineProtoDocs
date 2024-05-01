---
title: "updatePinnedSavedDialogs"
description: "Pinned saved dialogs » were updated"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePinnedSavedDialogs  
[Back to constructors index](/API_docs/constructors/index.html)



[Pinned saved dialogs »](https://core.telegram.org/api/saved-messages) were updated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|order|Array of [DialogPeer](/API_docs/types/DialogPeer.html) | Optional|New order of pinned saved dialogs|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updatePinnedSavedDialogs = ['_' => 'updatePinnedSavedDialogs', 'order' => [DialogPeer, DialogPeer]];
```  
