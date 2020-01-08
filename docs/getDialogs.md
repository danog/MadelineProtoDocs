---
title: getDialogs
description: getDialogs parameters, return type and example
redirect_from: /get_dialogs.html
---
## Method: getDialogs  

Gets full list of dialogs

### Return type: Array of [Peer objects](API_docs/types/Peer.md)

### Example ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
$Peers = yield $MadelineProto->getDialogs();
```

Or, if you're into Lua:

```lua
Peers = getDialogs()
```

