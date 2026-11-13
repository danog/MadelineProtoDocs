# messages.getDefaultTagReactions

> Fetch a default recommended list of [saved message tag reactions](https://core.telegram.org/api/saved-messages#tags).

[Back to methods index](index.html)



Fetch a default recommended list of [saved message tag reactions](https://core.telegram.org/api/saved-messages#tags).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | [Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation). | Optional|


### Return type: [messages.Reactions](/API_docs/types/messages.Reactions.html)

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

$messages_Reactions = $MadelineProto->messages->getDefaultTagReactions(hash: [$long\|string, $long\|string], );
```
