# contacts.importContactToken

> Obtain user info from a [temporary profile link](https://core.telegram.org/api/links#temporary-profile-links).

[Back to methods index](index.html)



Obtain user info from a [temporary profile link](https://core.telegram.org/api/links#temporary-profile-links).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|token|[string](/API_docs/types/string.html) | The token extracted from the [temporary profile link](https://core.telegram.org/api/links#temporary-profile-links). | Optional|


### Return type: [User](/API_docs/types/User.html)

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

$User = $MadelineProto->contacts->importContactToken(token: 'string', );
```
