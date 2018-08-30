---
title: NotifyPeer
description: constructors and methods of type NotifyPeer
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: NotifyPeer  
[Back to types index](index.md)



You can directly provide the [Update](Update.md) or [Message](Message.md) object here, MadelineProto will automatically extract the destination chat id.

The following syntaxes can also be used:

```
$NotifyPeer = '@username'; // Username

$NotifyPeer = 'me'; // The currently logged-in user

$NotifyPeer = 44700; // bot API id (users)
$NotifyPeer = -492772765; // bot API id (chats)
$NotifyPeer = -10038575794; // bot API id (channels)

$NotifyPeer = 'https://t.me/danogentili'; // t.me URLs
$NotifyPeer = 'https://t.me/joinchat/asfln1-21fa_'; // t.me invite links

$NotifyPeer = 'user#44700'; // tg-cli style id (users)
$NotifyPeer = 'chat#492772765'; // tg-cli style id (chats)
$NotifyPeer = 'channel#38575794'; // tg-cli style id (channels)
```

A [Chat](Chat.md), a [User](User.md), an [InputPeer](InputPeer.md), an [InputDialogPeer](InputDialogPeer.md), an [InputNotifyPeer](InputNotifyPeer.md), an [InputUser](InputUser.md), an [InputChannel](InputChannel.md), a [Peer](Peer.md), an [DialogPeer](DialogPeer.md), [NotifyPeer](NotifyPeer.md), or a [Chat](Chat.md) object can also be used.


### Possible values (constructors):

[notifyPeer](../constructors/notifyPeer.md)  

[notifyUsers](../constructors/notifyUsers.md)  

[notifyChats](../constructors/notifyChats.md)  

[notifyAll](../constructors/notifyAll.md)  



### Methods that return an object of this type (methods):



