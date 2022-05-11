---
title: Peer
description: constructors and methods of type Peer
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: Peer
[Back to types index](index.html)

You can directly provide the [Update](Update.html) or [Message](Message.html) object here, MadelineProto will automatically extract the destination chat id.

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

[peerUser](/API_docs/constructors/peerUser.html)  

[peerChat](/API_docs/constructors/peerChat.html)  

[peerChannel](/API_docs/constructors/peerChannel.html)  



### Methods that return an object of this type (methods):



[peerUser](/API_docs/constructors/peerUser.html)  

[peerChat](/API_docs/constructors/peerChat.html)  

[peerChannel](/API_docs/constructors/peerChannel.html)  

