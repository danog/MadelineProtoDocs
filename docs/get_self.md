---
title: get_self
description: get_self parameters, return type and example
---
## Method: get_self  

Gets info about the currently logged-in user.

No parameters

### Return type: [User object](API_docs/types/User.md)

### Example ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
$User = yield $MadelineProto->get_self();
```

Or, if you're into Lua:

```lua
User = get_self()
```

