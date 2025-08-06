---
title: "messages.updateSavedReactionTag"
description: "Update the [description of a saved message tag »](https://core.telegram.org/api/saved-messages#tags)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_updateSavedReactionTag.html
---
# Method: messages.updateSavedReactionTag
[Back to methods index](index.html)



Update the [description of a saved message tag »](https://core.telegram.org/api/saved-messages#tags).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|reaction|[Reaction](/API_docs/types/Reaction.html) | [Reaction](https://core.telegram.org/api/reactions) associated to the tag | Optional|
|title|[string](/API_docs/types/string.html) | Tag description, max 12 UTF-8 characters; to remove the description call the method without setting this flag. | Optional|


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

$Bool = $MadelineProto->messages->updateSavedReactionTag(reaction: $Reaction, title: 'string', );
```

