---
title: complete_signup
description: complete_signup parameters, return type and example
---
## Method: complete_signup  


### Parameters:

| Name     |    Type       |
|----------|---------------|
|first_name| A string with the first name|
|last_name| Optional, string with the last name|

### Return type: [auth.Authorization](API_docs/types/auth_Authorization.md)

### Example:


```php
$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->async(true);

[yield](ASYNC.html) $MadelineProto->phone_login(readline('Enter your phone number: '));
$authorization = [yield](ASYNC.html) $MadelineProto->complete_phone_login(readline('Enter the code you received: '));
if ($authorization['_'] === 'account.noPassword') {
    throw new \danog\MadelineProto\Exception('2FA is enabled but no password is set!');
}
if ($authorization['_'] === 'account.password') {
    $authorization = [yield](ASYNC.html) $MadelineProto->complete_2fa_login(readline('Please enter your password (hint '.$authorization['hint'].'): '));
}
if ($authorization['_'] === 'account.needSignup') {
    $authorization = [yield](ASYNC.html) $MadelineProto->complete_signup(readline('Please enter your first name: '), readline('Please enter your last name (can be empty): '));
}


```
