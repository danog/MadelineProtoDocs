---
title: InputDialogPeer
description: constructors and methods of type InputDialogPeer
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: InputDialogPeer
[Back to types index](index.md)

You can directly provide the [Update](Update.md) or [Message](Message.md) object here, MadelineProto will automatically extract the destination chat id.

The following syntaxes can also be used:

```php
$InputDialogPeer = '@username'; // Username

$InputDialogPeer = 'me'; // The currently logged-in user

$InputDialogPeer = 44700; // bot API id (users)
$InputDialogPeer = -492772765; // bot API id (chats)
$InputDialogPeer = -10038575794; // bot API id (channels)

$InputDialogPeer = 'https://t.me/danogentili'; // t.me URLs
$InputDialogPeer = 'https://t.me/joinchat/asfln1-21fa_'; // t.me invite links

$InputDialogPeer = 'user#44700'; // tg-cli style id (users)
$InputDialogPeer = 'chat#492772765'; // tg-cli style id (chats)
$InputDialogPeer = 'channel#38575794'; // tg-cli style id (channels)
```

A [Chat](Chat.md), a [User](User.md), an [InputPeer](InputPeer.md), an [InputDialogPeer](InputDialogPeer.md), an [InputNotifyPeer](InputNotifyPeer.md), an [InputUser](InputUser.md), an [InputChannel](InputChannel.md), a [Peer](Peer.md), an [DialogPeer](DialogPeer.md), [NotifyPeer](NotifyPeer.md), or a [Chat](Chat.md) object can also be used.




### Possible values (constructors):

[inputDialogPeer](../constructors/inputDialogPeer.md)  



### Methods that return an object of this type (methods):



[inputDialogPeer](../constructors/inputDialogPeer.md)  

