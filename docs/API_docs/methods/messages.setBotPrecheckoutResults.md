---
title: "messages.setBotPrecheckoutResults"
description: "Once the user has confirmed their payment and shipping details, the bot receives an [updateBotPrecheckoutQuery](../constructors/updateBotPrecheckoutQuery.html) update.  "
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setBotPrecheckoutResults.html
---
# Method: messages.setBotPrecheckoutResults
[Back to methods index](index.html)



Once the user has confirmed their payment and shipping details, the bot receives an [updateBotPrecheckoutQuery](../constructors/updateBotPrecheckoutQuery.html) update.  
Use this method to respond to such pre-checkout queries.  
**Note**: Telegram must receive an answer within 10 seconds after the pre-checkout query was sent.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|success|[Bool](/API_docs/types/Bool.html) | Set this flag if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order, otherwise do not set it, and set the `error` field, instead | Optional|
|query\_id|[long](/API_docs/types/long.html) | Unique identifier for the query to be answered | Yes|
|error|[string](/API_docs/types/string.html) | Required if the `success` isn't set. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. "Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!"). Telegram will display this message to the user. | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Bool = $MadelineProto->messages->setBotPrecheckoutResults(success: Bool, query_id: long, error: 'string', );
```

