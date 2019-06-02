---
title: contacts.importCard
description: Import card as contact
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.importCard  
[Back to methods index](index.md)


Import card as contact

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|export\_card|Array of [int](../types/int.md) | The card | Yes|


### Return type: [User](../types/User.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$User = $MadelineProto->contacts->importCard(['export_card' => [int, int], ]);
```

Or, if you're into Lua:

```lua
User = contacts.importCard({export_card={int}, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|EXPORT_CARD_INVALID|Provided card is invalid|
|NEED_MEMBER_INVALID|The provided member is invalid|


