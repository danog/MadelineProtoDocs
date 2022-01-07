---
title: "updateDialogUnreadMark"
description: "The manual unread mark of a chat was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDialogUnreadMark  
[Back to constructors index](index.md)



The manual unread mark of a chat was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|unread|[Bool](../types/Bool.md) | Optional|Was the chat marked or unmarked as read|
|peer|[DialogPeer](../types/DialogPeer.md) | Yes|The dialog|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDialogUnreadMark = ['_' => 'updateDialogUnreadMark', 'unread' => Bool, 'peer' => DialogPeer];
```  
