---
title: phoneLogin
description: phoneLogin parameters, return type and example
redirect_from: /phone_login.html
grand_parent: "Telegram RPC API"
parent: "Methods"
---
## Method: phoneLogin  


### Parameters:

| Name     |    Type       |
|----------|---------------|
|number| A string with the phone number, including the country code|

### Return type: [auth.SentCode](API_docs/types/auth.SentCode.html)

You must then use [completePhoneLogin](completePhoneLogin.html) 


### Example ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
$MadelineProto->phoneLogin(readline('Enter your phone number: '));
$authorization = $MadelineProto->completePhoneLogin(readline('Enter the code you received: '));
if ($authorization['_'] === 'account.noPassword') {
    throw new \danog\MadelineProto\Exception('2FA is enabled but no password is set!');
}
if ($authorization['_'] === 'account.password') {
    $authorization = $MadelineProto->complete2falogin(readline('Please enter your password (hint '.$authorization['hint'].'): '));
}
if ($authorization['_'] === 'account.needSignup') {
    $authorization = $MadelineProto->completeSignup(readline('Please enter your first name: '), readline('Please enter your last name (can be empty): '));
}

```

