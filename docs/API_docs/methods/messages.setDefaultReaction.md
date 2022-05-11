---
title: "messages.setDefaultReaction"
description: "Change default emoji reaction to use in the quick reaction menu: the value is synced across devices and can be fetched using [help.getAppConfig, `reactions_default` field](https://core.telegram.org/api/config#client-configuration)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setDefaultReaction.html
---
# Method: messages.setDefaultReaction
[Back to methods index](index.html)



Change default emoji reaction to use in the quick reaction menu: the value is synced across devices and can be fetched using [help.getAppConfig, `reactions_default` field](https://core.telegram.org/api/config#client-configuration).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|reaction|[string](/API_docs/types/string.html) | New emoji reaction | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Bool = $MadelineProto->messages->setDefaultReaction(reaction: 'string', );
```

