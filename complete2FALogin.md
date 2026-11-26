# complete2falogin

> complete2falogin parameters, return type and example

### Parameters:

| Name     |    Type       |
|----------|---------------|
|password| A string with the password|

### Return type: [auth.Authorization](API_docs/types/auth.Authorization.html)

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
