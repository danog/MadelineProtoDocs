---
title: NotifyPeer
description: constructors and methods of type NotifyPeer
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: NotifyPeer
[Back to types index](index.html)

You can directly provide the [Update](Update.html) or [Message](Message.html) object here, MadelineProto will automatically extract the destination chat id.

The following syntaxes can also be used:

```php
$NotifyPeer = '@username'; // Username

$NotifyPeer = $update; // Update objects received in the event handler

$NotifyPeer = 'me'; // The currently logged-in user

$NotifyPeer = 44700; // bot API id (users)
$NotifyPeer = -492772765; // bot API id (chats)
$NotifyPeer = -10038575794; // bot API id (channels)

$NotifyPeer = 'https://t.me/danogentili'; // t.me URLs
$NotifyPeer = 'https://t.me/joinchat/asfln1-21fa_'; // t.me invite links

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

[notifyPeer](/API_docs/constructors/notifyPeer.html)  

[notifyUsers](/API_docs/constructors/notifyUsers.html)  

[notifyChats](/API_docs/constructors/notifyChats.html)  

[notifyBroadcasts](/API_docs/constructors/notifyBroadcasts.html)  



### Methods that return an object of this type (methods):



[notifyPeer](/API_docs/constructors/notifyPeer.html)  

[notifyUsers](/API_docs/constructors/notifyUsers.html)  

[notifyChats](/API_docs/constructors/notifyChats.html)  

[notifyBroadcasts](/API_docs/constructors/notifyBroadcasts.html)  

