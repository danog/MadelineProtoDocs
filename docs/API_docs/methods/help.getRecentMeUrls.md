---
title: "help.getRecentMeUrls"
description: "Get recently used `t.me` links."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getRecentMeUrls.html
---
# Method: help.getRecentMeUrls
[Back to methods index](index.html)



Get recently used `t.me` links.

When installing official applications from "Download Telegram" buttons present in [t.me](https://t.me) pages, a referral parameter is passed to applications after installation.  
If, after downloading the application, the user creates a new account (instead of logging into an existing one), the referral parameter should be imported using this method, which returns the [t.me](https://t.me) pages the user recently opened, before installing Telegram.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|referer|[string](/API_docs/types/string.html) | Referrer | Optional|


### Return type: [help.RecentMeUrls](/API_docs/types/help.RecentMeUrls.html)

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

$help_RecentMeUrls = $MadelineProto->help->getRecentMeUrls(referer: 'string', );
```

