---
title: InputPeer
description: constructors and methods of type InputPeer
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: InputPeer
[Back to types index](index.html)

You can directly provide the [Update](Update.html) or [Message](Message.html) object here, MadelineProto will automatically extract the destination chat id.

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

[inputPeerEmpty](/API_docs/constructors/inputPeerEmpty.html)  

[inputPeerSelf](/API_docs/constructors/inputPeerSelf.html)  

[inputPeerChat](/API_docs/constructors/inputPeerChat.html)  

[inputPeerUser](/API_docs/constructors/inputPeerUser.html)  

[inputPeerChannel](/API_docs/constructors/inputPeerChannel.html)  

[inputPeerUserFromMessage](/API_docs/constructors/inputPeerUserFromMessage.html)  

[inputPeerChannelFromMessage](/API_docs/constructors/inputPeerChannelFromMessage.html)  



### Methods that return an object of this type (methods):



[inputPeerEmpty](/API_docs/constructors/inputPeerEmpty.html)  

[inputPeerSelf](/API_docs/constructors/inputPeerSelf.html)  

[inputPeerChat](/API_docs/constructors/inputPeerChat.html)  

[inputPeerUser](/API_docs/constructors/inputPeerUser.html)  

[inputPeerChannel](/API_docs/constructors/inputPeerChannel.html)  

[inputPeerUserFromMessage](/API_docs/constructors/inputPeerUserFromMessage.html)  

[inputPeerChannelFromMessage](/API_docs/constructors/inputPeerChannelFromMessage.html)  

