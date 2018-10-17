---
title: updateDialogPinned
description: updateDialogPinned attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDialogPinned  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|pinned|[Bool](../types/Bool.md) | Optional|
|peer|[DialogPeer](../types/DialogPeer.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDialogPinned = ['_' => 'updateDialogPinned', 'pinned' => Bool, 'peer' => DialogPeer];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateDialogPinned", "pinned": Bool, "peer": DialogPeer}
```


Or, if you're into Lua:

```lua
updateDialogPinned={_='updateDialogPinned', pinned=Bool, peer=DialogPeer}

```


