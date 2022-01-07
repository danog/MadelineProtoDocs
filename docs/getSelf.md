---
title: getSelf
description: getSelf parameters, return type and example
redirect_from: /get_self.html
grand_parent: "Telegram RPC API"
parent: "Methods"
---
## Method: getSelf  

Gets info about the currently logged-in user.

No parameters

### Return type: [User object](API_docs/types/User.html)

### Example ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
$User = yield $MadelineProto->getSelf();
```

Or, if you're into Lua:

```lua
User = getSelf()
```

