---
title: "stories.activateStealthMode"
description: "stories.activateStealthMode parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_activateStealthMode.html
---
# Method: stories.activateStealthMode
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|past|[Bool](/API_docs/types/Bool.html) | Optional|
|future|[Bool](/API_docs/types/Bool.html) | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->stories->activateStealthMode(past: $Bool, future: $Bool, );
```

