---
title: help.dismissSuggestion
description: Dismiss a suggestion
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_dismissSuggestion.html
---
# Method: help.dismissSuggestion
[Back to methods index](index.md)



Dismiss a suggestion

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|suggestion|[string](../types/string.md) | Suggestion | Yes|


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

$Bool = $MadelineProto->help->dismissSuggestion(['suggestion' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = help.dismissSuggestion({suggestion='string', })
```

