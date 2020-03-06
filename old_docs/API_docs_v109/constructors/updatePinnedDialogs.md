---
title: updatePinnedDialogs
description: Pinned dialogs were updated
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePinnedDialogs  
[Back to constructors index](index.md)



Pinned dialogs were updated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|folder\_id|[int](../types/int.md) | Optional|If the dialogs are in a folder, the folder ID|
|order|Array of [DialogPeer](../types/DialogPeer.md) | Optional|Order|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePinnedDialogs = ['_' => 'updatePinnedDialogs', 'folder_id' => int, 'order' => [DialogPeer, DialogPeer]];
```  


Or, if you're into Lua:

```lua
updatePinnedDialogs={_='updatePinnedDialogs', folder_id=int, order={DialogPeer}}

```


