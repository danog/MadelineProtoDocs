---
title: updateDialogUnreadMark
description: Update dialog unread mark
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDialogUnreadMark  
[Back to constructors index](index.md)



Update dialog unread mark

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|unread|[Bool](../types/Bool.md) | Optional|Unread?|
|peer|[DialogPeer](../types/DialogPeer.md) | Yes|Peer|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDialogUnreadMark = ['_' => 'updateDialogUnreadMark', 'unread' => Bool, 'peer' => DialogPeer];
```  


Or, if you're into Lua:

```lua
updateDialogUnreadMark={_='updateDialogUnreadMark', unread=Bool, peer=DialogPeer}

```


