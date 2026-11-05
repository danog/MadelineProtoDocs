# messages.getSuggestedDialogFilters

> Get [suggested folders](https://core.telegram.org/api/folders)

[Back to methods index](index.html)



Get [suggested folders](https://core.telegram.org/api/folders)



### Return type: [Vector\_of\_DialogFilterSuggested](/API_docs/types/DialogFilterSuggested.html)

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

$Vector_of_DialogFilterSuggested = $MadelineProto->messages->getSuggestedDialogFilters();
```
