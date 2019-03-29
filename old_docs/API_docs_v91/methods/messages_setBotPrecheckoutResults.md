---
title: messages.setBotPrecheckoutResults
description: Bots only: set precheckout results
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.setBotPrecheckoutResults  
[Back to methods index](index.md)


Bots only: set precheckout results

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|success|[Bool](../types/Bool.md) | Success? | Optional|
|query\_id|[long](../types/long.md) | Query ID | Yes|
|error|[string](../types/string.md) | Error | Optional|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->setBotPrecheckoutResults(['success' => Bool, 'query_id' => long, 'error' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = messages.setBotPrecheckoutResults({success=Bool, query_id=long, error='string', })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|ERROR_TEXT_EMPTY|The provided error message is empty|


