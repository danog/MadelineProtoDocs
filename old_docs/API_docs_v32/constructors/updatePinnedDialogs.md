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
|order|Array of [DialogPeer](../types/DialogPeer.md) | Optional|New order of pinned dialogs|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePinnedDialogs = ['_' => 'updatePinnedDialogs', 'order' => [DialogPeer, DialogPeer]];
```  


Or, if you're into Lua:

```lua
updatePinnedDialogs={_='updatePinnedDialogs', order={DialogPeer}}

```


