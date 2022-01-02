---
title: getPwrChat
description: getPwrChat parameters, return type and example
redirect_from: /get_pwr_chat.html
grand_parent: "Telegram RPC API"
parent: "Methods"
---
## Method: getPwrChat  


### Parameters:

| Name     |    Type       |
|----------|---------------|
|id| A username, a bot API chat id, a tg-cli chat id, a [Chat](API_docs/types/Chat.md), a [User](API_docs/types/User.md), an [InputPeer](API_docs/types/InputPeer.md), an [InputUser](API_docs/types/InputUser.md), an [InputChannel](API_docs/types/InputChannel.md), a [Peer](API_docs/types/Peer.md), or a [Chat](API_docs/types/Chat.md) object|
|fullfetch| Optional, a boolean that if set to true (the default) fetches full info (chat photo, invite link, bot info, common_chats_count, phone_calls_available, phone_calls_private, can_set_username, can_view_participants, participants)|

### Return type: [PWRTelegram Chat](Chat.md)

### Example ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
$Chat = yield $MadelineProto->getPwrChat($id);
```

Or, if you're into Lua:

```lua
Chat = getPwrChat(id)
```

