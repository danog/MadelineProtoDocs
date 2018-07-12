---
title: updateDialogUnreadMark
description: updateDialogUnreadMark attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDialogUnreadMark  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|unread|[Bool](../types/Bool.md) | Optional|
|peer|[DialogPeer](../types/DialogPeer.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```
$updateDialogUnreadMark = ['_' => 'updateDialogUnreadMark', 'unread' => Bool, 'peer' => DialogPeer];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateDialogUnreadMark", "unread": Bool, "peer": DialogPeer}
```


Or, if you're into Lua:  


```
updateDialogUnreadMark={_='updateDialogUnreadMark', unread=Bool, peer=DialogPeer}

```


