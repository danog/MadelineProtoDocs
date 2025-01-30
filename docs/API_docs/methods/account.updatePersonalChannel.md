---
title: "account.updatePersonalChannel"
description: "Associate (or remove) a personal [channel »](https://core.telegram.org/api/channel), that will be listed on our personal [profile page »](https://core.telegram.org/api/profile#personal-channel)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_updatePersonalChannel.html
---
# Method: account.updatePersonalChannel
[Back to methods index](index.html)



Associate (or remove) a personal [channel »](https://core.telegram.org/api/channel), that will be listed on our personal [profile page »](https://core.telegram.org/api/profile#personal-channel).

Changing it will emit an [updateUser](../constructors/updateUser.html) update.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | The channel, pass [inputChannelEmpty](../constructors/inputChannelEmpty.html) to remove it. | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->updatePersonalChannel(channel: $InputChannel, );
```

