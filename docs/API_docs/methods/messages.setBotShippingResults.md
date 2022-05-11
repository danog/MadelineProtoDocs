---
title: "messages.setBotShippingResults"
description: "If you sent an invoice requesting a shipping address and the parameter is\_flexible was specified, the bot will receive an [updateBotShippingQuery](../constructors/updateBotShippingQuery.html) update. Use this method to reply to shipping queries."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setBotShippingResults.html
---
# Method: messages.setBotShippingResults
[Back to methods index](index.html)



If you sent an invoice requesting a shipping address and the parameter is\_flexible was specified, the bot will receive an [updateBotShippingQuery](../constructors/updateBotShippingQuery.html) update. Use this method to reply to shipping queries.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|query\_id|[long](/API_docs/types/long.html) | Unique identifier for the query to be answered | Yes|
|error|[string](/API_docs/types/string.html) | Error message in human readable form that explains why it is impossible to complete the order (e.g. "Sorry, delivery to your desired address is unavailable"). Telegram will display this message to the user. | Optional|
|shipping\_options|Array of [ShippingOption](/API_docs/types/ShippingOption.html) | A vector of available shipping options. | Optional|


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
$Bool = $MadelineProto->messages->setBotShippingResults(query_id: long, error: 'string', shipping_options: [ShippingOption, ShippingOption], );
```

