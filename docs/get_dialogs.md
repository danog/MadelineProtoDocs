---
title: get_dialogs
description: get_dialogs parameters, return type and example
---
## Method: get_dialogs  

Gets full list of dialogs

### Return type: Array of [Peer objects](API_docs/types/Peer.md)

### Example:


```php
$MadelineProto = new \danog\MadelineProto\API();
$MadelineProto->start();

$Peers = $MadelineProto->get_dialogs();
```

Or, if you're into Lua:

```lua
Peers = get_dialogs()
```

