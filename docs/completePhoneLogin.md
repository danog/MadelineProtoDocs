---
title: completePhoneLogin
description: completePhoneLogin parameters, return type and example
redirect_from: /complete_phone_login.html
---
## Method: complete\_phone\_login  


### Parameters:

| Name     |    Type       |
|----------|---------------|
|code| A string with the phone code|

### Return type: [auth.Authorization](API_docs/types/auth.Authorization.md) or [account.Password](http://docs.madelineproto.xyz/API_docs/types/account_Password.html) or `['_' => 'account.needSignup']`

You must then use [complete2falogin](complete2FALogin.md) or [completeSignup](completeSignup.md) to login or signup, or simply start using `$MadelineProto` if the result is a `auth.Authorization` object.

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
