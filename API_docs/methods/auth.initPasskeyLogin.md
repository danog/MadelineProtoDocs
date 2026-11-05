# auth.initPasskeyLogin

> auth.initPasskeyLogin parameters, return type and example

[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|api\_id|[int](/API_docs/types/int.html) | Optional|
|api\_hash|[string](/API_docs/types/string.html) | Optional|


### Return type: [auth.PasskeyLoginOptions](/API_docs/types/auth.PasskeyLoginOptions.html)

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

$auth_PasskeyLoginOptions = $MadelineProto->auth->initPasskeyLogin(api_id: $int, api_hash: 'string', );
```
