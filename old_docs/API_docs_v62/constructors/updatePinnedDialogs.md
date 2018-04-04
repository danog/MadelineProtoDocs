---
title: updatePinnedDialogs
description: updatePinnedDialogs attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: updatePinnedDialogs  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|order|Array of [Peer](../types/Peer.md) | Optional|



### Type: [Update](../types/Update.md)


### Example:

```
$updatePinnedDialogs = ['_' => 'updatePinnedDialogs', 'order' => [Peer, Peer]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updatePinnedDialogs", "order": [Peer]}
```


Or, if you're into Lua:  


```
updatePinnedDialogs={_='updatePinnedDialogs', order={Peer}}

```


