---
title: updateDialogPinned
description: A dialog was pinned/unpinned
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDialogPinned  
[Back to constructors index](index.md)



A dialog was pinned/unpinned

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](../types/Bool.md) | Optional|Whether the dialog was pinned|
|folder\_id|[int](../types/int.md) | Optional|If the dialog is in a folder, the folder ID|
|peer|[DialogPeer](../types/DialogPeer.md) | Yes|The dialog|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDialogPinned = ['_' => 'updateDialogPinned', 'pinned' => Bool, 'folder_id' => int, 'peer' => DialogPeer];
```  


Or, if you're into Lua:

```lua
updateDialogPinned={_='updateDialogPinned', pinned=Bool, folder_id=int, peer=DialogPeer}

```


