# getPwrChat

> getPwrChat parameters, return type and example

### Parameters:

| Name     |    Type       |
|----------|---------------|
|id| A username, a bot API chat id, a [Chat](API_docs/types/Chat.html), a [User](API_docs/types/User.html), an [InputPeer](API_docs/types/InputPeer.html), an [InputUser](API_docs/types/InputUser.html), an [InputChannel](API_docs/types/InputChannel.html), a [Peer](API_docs/types/Peer.html), or a [Chat](API_docs/types/Chat.html) object|
|fullfetch| Optional, a boolean that if set to true (the default) fetches full info (chat photo, invite link, bot info, common_chats_count, phone_calls_available, phone_calls_private, can_set_username, can_view_participants, participants)|

### Return type: [PWRTelegram Chat](Chat.html)

### Example ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
$Chat = $MadelineProto->getPwrChat($id);
```
