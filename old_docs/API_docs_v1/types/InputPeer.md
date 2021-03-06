---
title: InputPeer
description: constructors and methods of type InputPeer
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: InputPeer
[Back to types index](index.md)

You can directly provide the [Update](Update.md) or [Message](Message.md) object here, MadelineProto will automatically extract the destination chat id.

The following syntaxes can also be used:

```php
$InputPeer = '@username'; // Username

$InputPeer = $update; // Update objects received in the event handler

$InputPeer = 'me'; // The currently logged-in user

$InputPeer = 44700; // bot API id (users)
$InputPeer = -492772765; // bot API id (chats)
$InputPeer = -10038575794; // bot API id (channels)

$InputPeer = 'https://t.me/danogentili'; // t.me URLs
$InputPeer = 'https://t.me/joinchat/asfln1-21fa_'; // t.me invite links

```

A [Chat](Chat.md), a [User](User.md), an [InputPeer](InputPeer.md), an [InputDialogPeer](InputDialogPeer.md), an [InputNotifyPeer](InputNotifyPeer.md), an [InputUser](InputUser.md), an [InputChannel](InputChannel.md), a [Peer](Peer.md), an [DialogPeer](DialogPeer.md), [NotifyPeer](NotifyPeer.md), or a [Chat](Chat.md) object can also be used.




### Possible values (constructors):

[inputPeerEmpty](../constructors/inputPeerEmpty.md)  

[inputPeerSelf](../constructors/inputPeerSelf.md)  

[inputPeerContact](../constructors/inputPeerContact.md)  

[inputPeerForeign](../constructors/inputPeerForeign.md)  

[inputPeerChat](../constructors/inputPeerChat.md)  



### Methods that return an object of this type (methods):



[inputPeerEmpty](../constructors/inputPeerEmpty.md)  

[inputPeerSelf](../constructors/inputPeerSelf.md)  

[inputPeerContact](../constructors/inputPeerContact.md)  

[inputPeerForeign](../constructors/inputPeerForeign.md)  

[inputPeerChat](../constructors/inputPeerChat.md)  

