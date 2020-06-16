---
title: contacts.importCard
description: contacts.importCard parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_importCard.html
---
# Method: contacts.importCard
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|export\_card|Array of [int](../types/int.md) | Yes|


### Return type: [User](../types/User.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$User = $MadelineProto->contacts->importCard(['export_card' => [int, int], ]);
```

Or, if you're into Lua:

```lua
User = contacts.importCard({export_card={int}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|EXPORT_CARD_INVALID|Provided card is invalid|


