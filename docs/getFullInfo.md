---
title: get_full_info
description: get_full_info parameters, return type and example
---
## Method: get_full_info  


### Parameters:

| Name     |    Type       |
|----------|---------------|
|id| A username, a bot API chat id, a tg-cli chat id, a [Chat](API_docs/types/Chat.md), a [User](API_docs/types/User.md), an [InputPeer](API_docs/types/InputPeer.md), an [InputUser](API_docs/types/InputUser.md), an [InputChannel](API_docs/types/InputChannel.md), a [Peer](API_docs/types/Peer.md), or a [Chat](API_docs/types/Chat.md) object|

### Return type: [FullInfo](FullInfo.md)

### Example ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
$Chat = yield $MadelineProto->getFullInfo($id);
```

Or, if you're into Lua:

```lua
Chat = getFullInfo(id)
```

