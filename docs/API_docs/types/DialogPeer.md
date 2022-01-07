---
title: DialogPeer
description: constructors and methods of type DialogPeer
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: DialogPeer
[Back to types index](index.html)

You can directly provide the [Update](Update.html) or [Message](Message.html) object here, MadelineProto will automatically extract the destination chat id.

The following syntaxes can also be used:

```php
$DialogPeer = '@username'; // Username

$DialogPeer = $update; // Update objects received in the event handler

$DialogPeer = 'me'; // The currently logged-in user

$DialogPeer = 44700; // bot API id (users)
$DialogPeer = -492772765; // bot API id (chats)
$DialogPeer = -10038575794; // bot API id (channels)

$DialogPeer = 'https://t.me/danogentili'; // t.me URLs
$DialogPeer = 'https://t.me/joinchat/asfln1-21fa_'; // t.me invite links

```

A [Chat](Chat.html), a [User](User.html), an [InputPeer](InputPeer.html), an [InputDialogPeer](InputDialogPeer.html), an [InputNotifyPeer](InputNotifyPeer.html), an [InputUser](InputUser.html), an [InputChannel](InputChannel.html), a [Peer](Peer.html), an [DialogPeer](DialogPeer.html), [NotifyPeer](NotifyPeer.html), or a [Chat](Chat.html) object can also be used.




### Possible values (constructors):

[dialogPeer](/API_docs/constructors/dialogPeer.html)  

[dialogPeerFolder](/API_docs/constructors/dialogPeerFolder.html)  



### Methods that return an object of this type (methods):

[$MadelineProto->messages->getDialogUnreadMarks](/API_docs/methods/messages.getDialogUnreadMarks.html)  



[dialogPeer](/API_docs/constructors/dialogPeer.html)  

[dialogPeerFolder](/API_docs/constructors/dialogPeerFolder.html)  

[$MadelineProto->messages->getDialogUnreadMarks](/API_docs/methods/messages.getDialogUnreadMarks.html)  

