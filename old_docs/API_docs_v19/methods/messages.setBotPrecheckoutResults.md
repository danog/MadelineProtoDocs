---
title: messages.setBotPrecheckoutResults
description: Once the user has confirmed their payment and shipping details, the bot receives an [updateBotPrecheckoutQuery](../constructors/updateBotPrecheckoutQuery.md) update.  
Use this method to respond to such pre-checkout queries.  
**Note**: Telegram must receive an answer within 10 seconds after the pre-checkout query was sent.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setBotPrecheckoutResults.html
---
# Method: messages.setBotPrecheckoutResults
[Back to methods index](index.md)



Once the user has confirmed their payment and shipping details, the bot receives an [updateBotPrecheckoutQuery](../constructors/updateBotPrecheckoutQuery.md) update.  
Use this method to respond to such pre-checkout queries.  
**Note**: Telegram must receive an answer within 10 seconds after the pre-checkout query was sent.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|success|[Bool](../types/Bool.md) | Set this flag if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order, otherwise do not set it, and set the `error` field, instead | Optional|
|query\_id|[long](../types/long.md) | Unique identifier for the query to be answered | Yes|
|error|[string](../types/string.md) | Required if the `success` isn't set. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. "Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!"). Telegram will display this message to the user. | Optional|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->setBotPrecheckoutResults(['success' => Bool, 'query_id' => long, 'error' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = messages.setBotPrecheckoutResults({success=Bool, query_id=long, error='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|ERROR_TEXT_EMPTY|The provided error message is empty|


