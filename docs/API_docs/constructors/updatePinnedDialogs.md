---
title: updatePinnedDialogs
description: updatePinnedDialogs attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePinnedDialogs  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|order|Array of [DialogPeer](../types/DialogPeer.md) | Optional|



### Type: [Update](../types/Update.md)


### Example:

```
$updatePinnedDialogs = ['_' => 'updatePinnedDialogs', 'order' => [DialogPeer, DialogPeer]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updatePinnedDialogs", "order": [DialogPeer]}
```


Or, if you're into Lua:  


```
updatePinnedDialogs={_='updatePinnedDialogs', order={DialogPeer}}

```


