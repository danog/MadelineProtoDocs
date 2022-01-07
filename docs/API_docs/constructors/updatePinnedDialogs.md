---
title: "updatePinnedDialogs"
description: "Pinned dialogs were updated"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePinnedDialogs  
[Back to constructors index](index.md)



Pinned dialogs were updated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|folder\_id|[int](../types/int.md) | Optional|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|
|order|Array of [DialogPeer](../types/DialogPeer.md) | Optional|New order of pinned dialogs|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePinnedDialogs = ['_' => 'updatePinnedDialogs', 'folder_id' => int, 'order' => [DialogPeer, DialogPeer]];
```  
