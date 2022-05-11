---
title: "updates.getDifference"
description: "You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling updates"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/updates_getDifference.html
---
# Method: updates.getDifference
[Back to methods index](index.html)



You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling updates

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|pts|[int](/API_docs/types/int.html) | PTS, see [updates](https://core.telegram.org/api/updates). | Yes|
|pts\_total\_limit|[int](/API_docs/types/int.html) | For fast updating: if provided and `pts + pts_total_limit < remote pts`, [updates.differenceTooLong](../constructors/updates.differenceTooLong.html) will be returned.<br>Simply tells the server to not return the difference if it is bigger than `pts_total_limit`<br>If the remote pts is too big (&gt; ~4000000), this field will default to 1000000 | Optional|
|date|[int](/API_docs/types/int.html) | date, see [updates](https://core.telegram.org/api/updates). | Yes|
|qts|[int](/API_docs/types/int.html) | QTS, see [updates](https://core.telegram.org/api/updates). | Yes|


### Return type: [updates.Difference](/API_docs/types/updates.Difference.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$updates_Difference = $MadelineProto->updates->getDifference(pts: int, pts_total_limit: int, date: int, qts: int, );
```

