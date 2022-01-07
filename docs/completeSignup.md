---
title: completeSignup
description: completeSignup parameters, return type and example
redirect_from: /complete_signup.html
grand_parent: "Telegram RPC API"
parent: "Methods"
---
## Method: completeSignup  


### Parameters:

| Name     |    Type       |
|----------|---------------|
|first_name| A string with the first name|
|last_name| Optional, string with the last name|

### Return type: [auth.Authorization](API_docs/types/auth.Authorization.html)

### Example ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
yield $MadelineProto->phoneLogin(readline('Enter your phone number: '));
$authorization = yield $MadelineProto->completePhoneLogin(readline('Enter the code you received: '));
if ($authorization['_'] === 'account.noPassword') {
    throw new \danog\MadelineProto\Exception('2FA is enabled but no password is set!');
}
if ($authorization['_'] === 'account.password') {
    $authorization = yield $MadelineProto->complete2falogin(readline('Please enter your password (hint '.$authorization['hint'].'): '));
}
if ($authorization['_'] === 'account.needSignup') {
    $authorization = yield $MadelineProto->completeSignup(readline('Please enter your first name: '), readline('Please enter your last name (can be empty): '));
}


```
