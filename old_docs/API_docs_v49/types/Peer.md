---
title: Peer
description: constructors and methods of type Peer
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: Peer
[Back to types index](index.md)

You can directly provide the [Update](Update.md) or [Message](Message.md) object here, MadelineProto will automatically extract the destination chat id.

The following syntaxes can also be used:

```php
$Peer = '@username'; // Username

$Peer = $update; // Update objects received in the event handler

$Peer = 'me'; // The currently logged-in user

$Peer = 44700; // bot API id (users)
$Peer = -492772765; // bot API id (chats)
$Peer = -10038575794; // bot API id (channels)

$Peer = 'https://t.me/danogentili'; // t.me URLs
$Peer = 'https://t.me/joinchat/asfln1-21fa_'; // t.me invite links

```

A [Chat](Chat.md), a [User](User.md), an [InputPeer](InputPeer.md), an [InputDialogPeer](InputDialogPeer.md), an [InputNotifyPeer](InputNotifyPeer.md), an [InputUser](InputUser.md), an [InputChannel](InputChannel.md), a [Peer](Peer.md), an [DialogPeer](DialogPeer.md), [NotifyPeer](NotifyPeer.md), or a [Chat](Chat.md) object can also be used.




### Possible values (constructors):

[peerUser](../constructors/peerUser.md)  

[peerChat](../constructors/peerChat.md)  

[peerChannel](../constructors/peerChannel.md)  



### Methods that return an object of this type (methods):



[peerUser](../constructors/peerUser.md)  

[peerChat](../constructors/peerChat.md)  

[peerChannel](../constructors/peerChannel.md)  

