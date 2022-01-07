---
title: User
description: constructors and methods of type User
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: User
[Back to types index](index.html)

You can directly provide the [Update](Update.html) or [Message](Message.html) object here, MadelineProto will automatically extract the destination chat id.

The following syntaxes can also be used:

```php
$User = '@username'; // Username

$User = $update; // Update objects received in the event handler

$User = 'me'; // The currently logged-in user

$User = 44700; // bot API id (users)
$User = -492772765; // bot API id (chats)
$User = -10038575794; // bot API id (channels)

$User = 'https://t.me/danogentili'; // t.me URLs
$User = 'https://t.me/joinchat/asfln1-21fa_'; // t.me invite links

```

A [Chat](Chat.html), a [User](User.html), an [InputPeer](InputPeer.html), an [InputDialogPeer](InputDialogPeer.html), an [InputNotifyPeer](InputNotifyPeer.html), an [InputUser](InputUser.html), an [InputChannel](InputChannel.html), a [Peer](Peer.html), an [DialogPeer](DialogPeer.html), [NotifyPeer](NotifyPeer.html), or a [Chat](Chat.html) object can also be used.




### Possible values (constructors):

[userEmpty](/API_docs/constructors/userEmpty.html)  

[user](/API_docs/constructors/user.html)  



### Methods that return an object of this type (methods):

[$MadelineProto->account->updateProfile](/API_docs/methods/account.updateProfile.html)  

[$MadelineProto->account->updateUsername](/API_docs/methods/account.updateUsername.html)  

[$MadelineProto->account->changePhone](/API_docs/methods/account.changePhone.html)  

[$MadelineProto->users->getUsers](/API_docs/methods/users.getUsers.html)  



[userEmpty](/API_docs/constructors/userEmpty.html)  

[user](/API_docs/constructors/user.html)  

[$MadelineProto->account->updateProfile](/API_docs/methods/account.updateProfile.html)  

[$MadelineProto->account->updateUsername](/API_docs/methods/account.updateUsername.html)  

[$MadelineProto->account->changePhone](/API_docs/methods/account.changePhone.html)  

[$MadelineProto->users->getUsers](/API_docs/methods/users.getUsers.html)  

