# contacts.getSaved

> Get all contacts, requires a [takeout session, see here » for more info](https://core.telegram.org/api/takeout).

[Back to methods index](index.html)



Get all contacts, requires a [takeout session, see here » for more info](https://core.telegram.org/api/takeout).



### Return type: [Vector\_of\_SavedContact](/API_docs/types/SavedContact.html)

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

$Vector_of_SavedContact = $MadelineProto->contacts->getSaved();
```
