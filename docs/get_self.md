---
title: get_self
description: get_self parameters, return type and example
---
## Method: get_self  

Gets info about the currently logged-in user.

No parameters

### Return type: [User object](API_docs/types/User.md)

### Example:


```php
$MadelineProto = new \danog\MadelineProto\API();
$MadelineProto->start();

$User = [yield](ASYNC.html) $MadelineProto->get_self();
```

Or, if you're into Lua:

```lua
User = get_self()
```

