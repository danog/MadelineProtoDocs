---
title: DialogPeer
description: constructors and methods of type DialogPeer
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: DialogPeer
[Back to types index](index.md)

You can directly provide the [Update](Update.md) or [Message](Message.md) object here, MadelineProto will automatically extract the destination chat id.

The following syntaxes can also be used:

```php
$DialogPeer = '@username'; // Username

$DialogPeer = 'me'; // The currently logged-in user

$DialogPeer = 44700; // bot API id (users)
$DialogPeer = -492772765; // bot API id (chats)
$DialogPeer = -10038575794; // bot API id (channels)

$DialogPeer = 'https://t.me/danogentili'; // t.me URLs
$DialogPeer = 'https://t.me/joinchat/asfln1-21fa_'; // t.me invite links

$DialogPeer = 'user#44700'; // tg-cli style id (users)
$DialogPeer = 'chat#492772765'; // tg-cli style id (chats)
$DialogPeer = 'channel#38575794'; // tg-cli style id (channels)
```

A [Chat](Chat.md), a [User](User.md), an [InputPeer](InputPeer.md), an [InputDialogPeer](InputDialogPeer.md), an [InputNotifyPeer](InputNotifyPeer.md), an [InputUser](InputUser.md), an [InputChannel](InputChannel.md), a [Peer](Peer.md), an [DialogPeer](DialogPeer.md), [NotifyPeer](NotifyPeer.md), or a [Chat](Chat.md) object can also be used.




### Possible values (constructors):

[dialogPeer](../constructors/dialogPeer.md)  



### Methods that return an object of this type (methods):



[dialogPeer](../constructors/dialogPeer.md)  

