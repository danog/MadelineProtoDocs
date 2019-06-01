---
title: Getting info about the current user
description: Here's how you can fetch info about the currently logged in user
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Getting info about the current user

Here's how you can fetch info about the currently logged in user

```php
$me = yield $MadelineProto->get_self();

\danog\MadelineProto\Logger::log("Hi ".$me['first_name']."!");
```

[`get_self`](https://docs.madelineproto.xyz/get_self.html) returns a [User object](../API_docs/types/User.html) that contains info about the currently logged in user/bot, or false if the current instance is not logged in.

<a href="https://docs.madelineproto.xyz/docs/EXCEPTIONS.html">Next section</a>