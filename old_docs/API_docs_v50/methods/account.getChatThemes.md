---
title: account.getChatThemes
description: account.getChatThemes parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getChatThemes.html
---
# Method: account.getChatThemes
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|Array of [int](../types/int.md) | Optional|


### Return type: [account.ChatThemes](../types/account.ChatThemes.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_ChatThemes = $MadelineProto->account->getChatThemes(['hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
account_ChatThemes = account.getChatThemes({hash={int}, })
```

