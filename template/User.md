You can directly provide the [Update](Update.md) or [Message](Message.md) object here, MadelineProto will automatically extract the destination chat id.

The following syntaxes can also be used:

```php
$%1$s = '@username'; // Username

$%1$s = 'me'; // The currently logged-in user

$%1$s = 44700; // bot API id (users)
$%1$s = -492772765; // bot API id (chats)
$%1$s = -10038575794; // bot API id (channels)

$%1$s = 'https://t.me/danogentili'; // t.me URLs
$%1$s = 'https://t.me/joinchat/asfln1-21fa_'; // t.me invite links

$%1$s = 'user#44700'; // tg-cli style id (users)
$%1$s = 'chat#492772765'; // tg-cli style id (chats)
$%1$s = 'channel#38575794'; // tg-cli style id (channels)
```

A [Chat](Chat.md), a [User](User.md), an [InputPeer](InputPeer.md), an [InputDialogPeer](InputDialogPeer.md), an [InputNotifyPeer](InputNotifyPeer.md), an [InputUser](InputUser.md), an [InputChannel](InputChannel.md), a [Peer](Peer.md), an [DialogPeer](DialogPeer.md), [NotifyPeer](NotifyPeer.md), or a [Chat](Chat.md) object can also be used.


