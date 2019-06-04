---
title: get_full_dialogs
description: get_full_dialogs parameters, return type and example
---
## Method: get_dialogs  

Gets full list of dialogs

### Return type: Array of [Dialog objects](API_docs/types/Dialog.md)

### Example ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
$Dialogs = yield $MadelineProto->get_full_dialogs();
```

Or, if you're into Lua:

```lua
Dialogs = get_full_dialogs()
```

