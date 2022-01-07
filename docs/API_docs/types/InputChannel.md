---
title: InputChannel
description: constructors and methods of type InputChannel
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: InputChannel
[Back to types index](index.md)

You can directly provide the [Update](Update.md) or [Message](Message.md) object here, MadelineProto will automatically extract the destination chat id.

The following syntaxes can also be used:

```php
$InputChannel = '@username'; // Username

$InputChannel = $update; // Update objects received in the event handler

$InputChannel = 'me'; // The currently logged-in user

$InputChannel = 44700; // bot API id (users)
$InputChannel = -492772765; // bot API id (chats)
$InputChannel = -10038575794; // bot API id (channels)

$InputChannel = 'https://t.me/danogentili'; // t.me URLs
$InputChannel = 'https://t.me/joinchat/asfln1-21fa_'; // t.me invite links

```

A [Chat](Chat.md), a [User](User.md), an [InputPeer](InputPeer.md), an [InputDialogPeer](InputDialogPeer.md), an [InputNotifyPeer](InputNotifyPeer.md), an [InputUser](InputUser.md), an [InputChannel](InputChannel.md), a [Peer](Peer.md), an [DialogPeer](DialogPeer.md), [NotifyPeer](NotifyPeer.md), or a [Chat](Chat.md) object can also be used.




### Possible values (constructors):

[inputChannelEmpty](/API_docs/constructors/inputChannelEmpty.md)  

[inputChannel](/API_docs/constructors/inputChannel.md)  

[inputChannelFromMessage](/API_docs/constructors/inputChannelFromMessage.md)  



### Methods that return an object of this type (methods):



[inputChannelEmpty](/API_docs/constructors/inputChannelEmpty.md)  

[inputChannel](/API_docs/constructors/inputChannel.md)  

[inputChannelFromMessage](/API_docs/constructors/inputChannelFromMessage.md)  

