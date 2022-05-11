---
title: InputChannel
description: constructors and methods of type InputChannel
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: InputChannel
[Back to types index](index.html)

You can directly provide the [Update](Update.html) or [Message](Message.html) object here, MadelineProto will automatically extract the destination chat id.

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

[inputChannelEmpty](/API_docs/constructors/inputChannelEmpty.html)  

[inputChannel](/API_docs/constructors/inputChannel.html)  

[inputChannelFromMessage](/API_docs/constructors/inputChannelFromMessage.html)  



### Methods that return an object of this type (methods):



[inputChannelEmpty](/API_docs/constructors/inputChannelEmpty.html)  

[inputChannel](/API_docs/constructors/inputChannel.html)  

[inputChannelFromMessage](/API_docs/constructors/inputChannelFromMessage.html)  

