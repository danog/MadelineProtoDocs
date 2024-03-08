---
title: "stories.activateStealthMode"
description: "Activates [stories stealth mode](https://core.telegram.org/api/stories#stealth-mode), see [here »](https://core.telegram.org/api/stories#stealth-mode) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_activateStealthMode.html
---
# Method: stories.activateStealthMode
[Back to methods index](index.html)



Activates [stories stealth mode](https://core.telegram.org/api/stories#stealth-mode), see [here »](https://core.telegram.org/api/stories#stealth-mode) for more info.

Will return an [updateStoriesStealthMode](../constructors/updateStoriesStealthMode.html).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|past|[Bool](/API_docs/types/Bool.html) | Whether to erase views from any stories opened in the past [`stories_stealth_past_period` seconds »](https://core.telegram.org/api/config#stories-stealth-past-period), as specified by the [client configuration](https://core.telegram.org/api/config#client-configuration). | Optional|
|future|[Bool](/API_docs/types/Bool.html) | Whether to hide future story views for the next [`stories_stealth_future_period` seconds »](https://core.telegram.org/api/config#stories-stealth-future-period), as specified by the [client configuration](https://core.telegram.org/api/config#client-configuration). | Optional|


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

