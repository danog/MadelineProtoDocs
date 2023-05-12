---
title: getId
description: getId parameters, return type and example
grand_parent: "Telegram RPC API"
parent: "Methods"
---
## Method: getId


### Parameters:

| Name     |    Type       |
|----------|---------------|
|id| A username, a bot API chat id, a tg-cli chat id, a [Chat](API_docs/types/Chat.html), a [User](API_docs/types/User.html), an [InputPeer](API_docs/types/InputPeer.html), an [InputUser](API_docs/types/InputUser.html), an [InputChannel](API_docs/types/InputChannel.html), a [Peer](API_docs/types/Peer.html), or a [Chat](API_docs/types/Chat.html) object|

### Return type: integer

### Example ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
$id = $MadelineProto->getId($id);
```

