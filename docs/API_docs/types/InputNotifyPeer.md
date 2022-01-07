---
title: InputNotifyPeer
description: constructors and methods of type InputNotifyPeer
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: InputNotifyPeer
[Back to types index](index.md)

You can directly provide the [Update](Update.md) or [Message](Message.md) object here, MadelineProto will automatically extract the destination chat id.

The following syntaxes can also be used:

```php
$InputNotifyPeer = '@username'; // Username

$InputNotifyPeer = $update; // Update objects received in the event handler

$InputNotifyPeer = 'me'; // The currently logged-in user

$InputNotifyPeer = 44700; // bot API id (users)
$InputNotifyPeer = -492772765; // bot API id (chats)
$InputNotifyPeer = -10038575794; // bot API id (channels)

$InputNotifyPeer = 'https://t.me/danogentili'; // t.me URLs
$InputNotifyPeer = 'https://t.me/joinchat/asfln1-21fa_'; // t.me invite links

```

A [Chat](Chat.md), a [User](User.md), an [InputPeer](InputPeer.md), an [InputDialogPeer](InputDialogPeer.md), an [InputNotifyPeer](InputNotifyPeer.md), an [InputUser](InputUser.md), an [InputChannel](InputChannel.md), a [Peer](Peer.md), an [DialogPeer](DialogPeer.md), [NotifyPeer](NotifyPeer.md), or a [Chat](Chat.md) object can also be used.




### Possible values (constructors):

[inputNotifyPeer](/API_docs/constructors/inputNotifyPeer.md)  

[inputNotifyUsers](/API_docs/constructors/inputNotifyUsers.md)  

[inputNotifyChats](/API_docs/constructors/inputNotifyChats.md)  

[inputNotifyBroadcasts](/API_docs/constructors/inputNotifyBroadcasts.md)  



### Methods that return an object of this type (methods):



[inputNotifyPeer](/API_docs/constructors/inputNotifyPeer.md)  

[inputNotifyUsers](/API_docs/constructors/inputNotifyUsers.md)  

[inputNotifyChats](/API_docs/constructors/inputNotifyChats.md)  

[inputNotifyBroadcasts](/API_docs/constructors/inputNotifyBroadcasts.md)  

