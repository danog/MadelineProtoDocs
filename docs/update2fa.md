---
title: update2fa
description: Update 2FA password
redirect_from: /update_2fa.html
grand_parent: "Telegram RPC API"
parent: "Methods"
---
## Method: update2fa  

The params array can contain password (current password), new_password, email (optional) and hint params.

### Parameters:

| Name     |    Type       |
|----------|---------------|
|params|An array of parameters|

### Return type: [Bool](API_docs/types/Bool.html)

### Example ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
try {
    yield $MadelineProto->update2fa(['password' => 'current password', 'new_password' => 'New password', 'email' => 'daniil@daniil.it', 'hint' => 'ponies']);
} catch (RPCErrorException $e) {
    if (strpos($e->rpc, 'EMAIL_UNCONFIRMED_') !== false) {
        $Bool = yield $MadelineProto->account->confirmPasswordEmail(['code' => yield $MadelineProto->readline('Enter your email code: ')]);
    } else {
        throw $e;
    }
}
```
