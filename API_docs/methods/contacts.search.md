# contacts.search

> Returns users found by username substring.

[Back to methods index](index.html)



Returns users found by username substring.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|broadcasts|[Bool](/API_docs/types/Bool.html) |  | Optional|
|bots|[Bool](/API_docs/types/Bool.html) |  | Optional|
|q|[string](/API_docs/types/string.html) | Target substring | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of users to be returned | Optional|


### Return type: [contacts.Found](/API_docs/types/contacts.Found.html)

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

$contacts_Found = $MadelineProto->contacts->search(broadcasts: $Bool, bots: $Bool, q: 'string', limit: $int, );
```
