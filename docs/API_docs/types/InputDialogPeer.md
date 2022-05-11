---
title: InputDialogPeer
description: constructors and methods of type InputDialogPeer
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: InputDialogPeer
[Back to types index](index.html)

You can directly provide the [Update](Update.html) or [Message](Message.html) object here, MadelineProto will automatically extract the destination chat id.

The following syntaxes can also be used:

```php
$InputDialogPeer = '@username'; // Username

$InputDialogPeer = $update; // Update objects received in the event handler

$InputDialogPeer = 'me'; // The currently logged-in user

$InputDialogPeer = 44700; // bot API id (users)
$InputDialogPeer = -492772765; // bot API id (chats)
$InputDialogPeer = -10038575794; // bot API id (channels)

$InputDialogPeer = 'https://t.me/danogentili'; // t.me URLs
$InputDialogPeer = 'https://t.me/joinchat/asfln1-21fa_'; // t.me invite links

```

You can also provide one of the following objects, instead, MadelineProto will handle conversion automatically:  

- [Chat](Chat.html)
- [User](User.html)
- [InputPeer](InputPeer.html)
- [InputDialogPeer](InputDialogPeer.html)
- [InputNotifyPeer](InputNotifyPeer.html)
- [InputUser](InputUser.html)
- [InputChannel](InputChannel.html)
- [Peer](Peer.html)
- [DialogPeer](DialogPeer.html)
- [NotifyPeer](NotifyPeer.html)
- [Chat](Chat.html)




### Possible values (constructors):

[inputDialogPeer](/API_docs/constructors/inputDialogPeer.html)  

[inputDialogPeerFolder](/API_docs/constructors/inputDialogPeerFolder.html)  



### Methods that return an object of this type (methods):



[inputDialogPeer](/API_docs/constructors/inputDialogPeer.html)  

[inputDialogPeerFolder](/API_docs/constructors/inputDialogPeerFolder.html)  

