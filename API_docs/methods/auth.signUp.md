# auth.signUp

> You cannot use this method directly, use the completeSignup method instead (see https://docs.madelineproto.xyz for more info)

[Back to methods index](index.html)



You cannot use this method directly, use the completeSignup method instead (see https://docs.madelineproto.xyz for more info)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|no\_joined\_notifications|[Bool](/API_docs/types/Bool.html) | If set, users on Telegram that have already added `phone_number` to their contacts will *not* receive signup notifications about this user. | Optional|
|phone\_number|[string](/API_docs/types/string.html) | Phone number in the international format | Optional|
|phone\_code\_hash|[string](/API_docs/types/string.html) | SMS-message ID | Optional|
|first\_name|[string](/API_docs/types/string.html) | New user first name | Optional|
|last\_name|[string](/API_docs/types/string.html) | New user last name | Optional|


### Return type: [auth.Authorization](/API_docs/types/auth.Authorization.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth_Authorization = $MadelineProto->auth->signUp(no_joined_notifications: $Bool, phone_number: 'string', phone_code_hash: 'string', first_name: 'string', last_name: 'string', );
```
