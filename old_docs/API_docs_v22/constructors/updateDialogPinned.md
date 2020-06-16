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
|peer|[Peer](../types/Peer.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDialogPinned = ['_' => 'updateDialogPinned', 'pinned' => Bool, 'peer' => Peer];
```  


Or, if you're into Lua:

```lua
updateDialogPinned={_='updateDialogPinned', pinned=Bool, peer=Peer}

```


