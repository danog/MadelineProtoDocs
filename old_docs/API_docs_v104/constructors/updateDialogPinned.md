---
title: updateDialogPinned
description: Update dialog pinned
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDialogPinned  
[Back to constructors index](index.md)



Update dialog pinned

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](../types/Bool.md) | Optional|Pinned?|
|folder\_id|[int](../types/int.md) | Optional|Folder ID|
|peer|[DialogPeer](../types/DialogPeer.md) | Yes|Peer|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDialogPinned = ['_' => 'updateDialogPinned', 'pinned' => Bool, 'folder_id' => int, 'peer' => DialogPeer];
```  


Or, if you're into Lua:

```lua
updateDialogPinned={_='updateDialogPinned', pinned=Bool, folder_id=int, peer=DialogPeer}

```


