---
title: help.getInviteText
description: Returns localized text of a text message with an invitation.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getInviteText.html
---
# Method: help.getInviteText
[Back to methods index](index.md)



Returns localized text of a text message with an invitation.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|lang\_code|[string](../types/string.md) |  | Yes|


### Return type: [help.InviteText](../types/help.InviteText.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help.InviteText = $MadelineProto->help->getInviteText(['lang_code' => 'string', ]);
```

Or, if you're into Lua:

```lua
help.InviteText = help.getInviteText({lang_code='string', })
```

