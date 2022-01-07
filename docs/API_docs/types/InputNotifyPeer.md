---
title: InputNotifyPeer
description: constructors and methods of type InputNotifyPeer
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: InputNotifyPeer
[Back to types index](index.html)

You can directly provide the [Update](Update.html) or [Message](Message.html) object here, MadelineProto will automatically extract the destination chat id.

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

A [Chat](Chat.html), a [User](User.html), an [InputPeer](InputPeer.html), an [InputDialogPeer](InputDialogPeer.html), an [InputNotifyPeer](InputNotifyPeer.html), an [InputUser](InputUser.html), an [InputChannel](InputChannel.html), a [Peer](Peer.html), an [DialogPeer](DialogPeer.html), [NotifyPeer](NotifyPeer.html), or a [Chat](Chat.html) object can also be used.




### Possible values (constructors):

[inputNotifyPeer](/API_docs/constructors/inputNotifyPeer.html)  

[inputNotifyUsers](/API_docs/constructors/inputNotifyUsers.html)  

[inputNotifyChats](/API_docs/constructors/inputNotifyChats.html)  

[inputNotifyBroadcasts](/API_docs/constructors/inputNotifyBroadcasts.html)  



### Methods that return an object of this type (methods):



[inputNotifyPeer](/API_docs/constructors/inputNotifyPeer.html)  

[inputNotifyUsers](/API_docs/constructors/inputNotifyUsers.html)  

[inputNotifyChats](/API_docs/constructors/inputNotifyChats.html)  

[inputNotifyBroadcasts](/API_docs/constructors/inputNotifyBroadcasts.html)  

