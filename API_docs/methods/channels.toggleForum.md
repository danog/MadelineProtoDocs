# channels.toggleForum

> Enable or disable [forum functionality](https://core.telegram.org/api/forum) in a supergroup.

[Back to methods index](index.html)



Enable or disable [forum functionality](https://core.telegram.org/api/forum) in a supergroup.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Supergroup ID | Optional|
|enabled|[Bool](/API_docs/types/Bool.html) | Enable or disable forum functionality | Yes|
|tabs|[Bool](/API_docs/types/Bool.html) | If true enables the tabbed forum UI, otherwise enables the list-based forum UI. | Yes|
|sidebar|[Bool](/API_docs/types/Bool.html) |  | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->channels->toggleForum(channel: $InputChannel, enabled: $Bool, tabs: $Bool, sidebar: $Bool, );
```
