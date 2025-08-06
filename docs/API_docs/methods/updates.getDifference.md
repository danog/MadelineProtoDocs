---
title: "updates.getDifference"
description: "You cannot use this method directly, please use the [event handler](https://docs.madelineproto.xyz/docs/UPDATES.html), instead."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/updates_getDifference.html
---
# Method: updates.getDifference
[Back to methods index](index.html)



# Warning: this is a low-level, complex method that **must never** be used directly.
The [event handler](https://docs.madelineproto.xyz/docs/UPDATES.html) provides a high-level abstraction that **must** be used instead of this method to fetch updates.
If you want to fetch all users of a bot using a bot token, use [getDialogIds](https://docs.madelineproto.xyz/docs/DIALOGS.html) or the high-level [broadcast API](https://docs.madelineproto.xyz/docs/BROADCAST.html), instead.

You cannot use this method directly, please use the [event handler](https://docs.madelineproto.xyz/docs/UPDATES.html), instead.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|pts|[int](/API_docs/types/int.html) | PTS, see [updates](https://core.telegram.org/api/updates). | Optional|
|pts\_limit|[int](/API_docs/types/int.html) | PTS limit | Optional|
|pts\_total\_limit|[int](/API_docs/types/int.html) | For fast updating: if provided and `pts + pts_total_limit < remote pts`, [updates.differenceTooLong](../constructors/updates.differenceTooLong.html) will be returned.<br>Simply tells the server to not return the difference if it is bigger than `pts_total_limit`<br>If the remote pts is too big (&gt; ~4000000), this field will default to 1000000 | Optional|
|date|[int](/API_docs/types/int.html) | date, see [updates](https://core.telegram.org/api/updates). | Optional|
|qts|[int](/API_docs/types/int.html) | QTS, see [updates](https://core.telegram.org/api/updates). | Optional|
|qts\_limit|[int](/API_docs/types/int.html) | QTS limit | Optional|


### Return type: [updates.Difference](/API_docs/types/updates.Difference.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$updates_Difference = $MadelineProto->updates->getDifference(pts: $int, pts_limit: $int, pts_total_limit: $int, date: $int, qts: $int, qts_limit: $int, );
```

