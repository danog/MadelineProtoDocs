# account.reorderUsernames

> Reorder usernames associated with the currently logged-in user.

[Back to methods index](index.html)



Reorder usernames associated with the currently logged-in user.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|order|Array of [string](/API_docs/types/string.html) | The new order for active usernames. All active usernames must be specified. | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->account->reorderUsernames(order: ['string', 'string'], );
```
