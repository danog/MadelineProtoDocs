---
title: "account.updateBusinessGreetingMessage"
description: "Set a list of [Telegram Business greeting messages](https://core.telegram.org/api/business#greeting-messages)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_updateBusinessGreetingMessage.html
---
# Method: account.updateBusinessGreetingMessage
[Back to methods index](index.html)



Set a list of [Telegram Business greeting messages](https://core.telegram.org/api/business#greeting-messages).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|message|[InputBusinessGreetingMessage](/API_docs/types/InputBusinessGreetingMessage.html) | Greeting message configuration and contents. | Optional|


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

$Bool = $MadelineProto->account->updateBusinessGreetingMessage(message: $InputBusinessGreetingMessage, );
```


## Return value 

If the length of the provided message is bigger than 4096, the message will be split in chunks and the method will be called multiple times, with the same parameters (except for the message), and an array of [Bool](../types/Bool.html) will be returned instead.


