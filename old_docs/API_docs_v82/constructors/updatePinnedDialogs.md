---
title: updatePinnedDialogs
description: Update pinned dialogs
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePinnedDialogs  
[Back to constructors index](index.md)



Update pinned dialogs

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|order|Array of [DialogPeer](../types/DialogPeer.md) | Optional|Order|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePinnedDialogs = ['_' => 'updatePinnedDialogs', 'order' => [DialogPeer, DialogPeer]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updatePinnedDialogs", "order": [DialogPeer]}
```


Or, if you're into Lua:

```lua
updatePinnedDialogs={_='updatePinnedDialogs', order={DialogPeer}}

```


