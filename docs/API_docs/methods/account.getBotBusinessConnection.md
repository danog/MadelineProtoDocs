---
title: "account.getBotBusinessConnection"
description: "Bots may invoke this method to re-fetch the [updateBotBusinessConnect](../constructors/updateBotBusinessConnect.html) constructor associated with a specific [business `connection_id`, see here »](https://core.telegram.org/api/business#connected-bots) for more info on connected business bots.  "
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getBotBusinessConnection.html
---
# Method: account.getBotBusinessConnection
[Back to methods index](index.html)



Bots may invoke this method to re-fetch the [updateBotBusinessConnect](../constructors/updateBotBusinessConnect.html) constructor associated with a specific [business `connection_id`, see here »](https://core.telegram.org/api/business#connected-bots) for more info on connected business bots.  
This is needed for example for freshly logged in bots that are receiving some [updateBotNewBusinessMessage](../constructors/updateBotNewBusinessMessage.html), etc. updates because some users have already connected to the bot before it could login.  
In this case, the bot is receiving messages from the business connection, but it hasn't cached the associated [updateBotBusinessConnect](../constructors/updateBotBusinessConnect.html) with info about the connection (can it reply to messages? etc.) yet, and cannot receive the old ones because they were sent when the bot wasn't logged into the session yet.  
This method can be used to fetch info about a not-yet-cached business connection, and should not be invoked if the info is already cached or to fetch changes, as eventual changes will automatically be sent as new [updateBotBusinessConnect](../constructors/updateBotBusinessConnect.html) updates to the bot using the usual [update delivery methods »](https://core.telegram.org/api/updates).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|connection\_id|[string](/API_docs/types/string.html) | [Business connection ID »](https://core.telegram.org/api/business#connected-bots). | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can userbots use this method: **YES**

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->account->getBotBusinessConnection(connection_id: 'string', );
```

