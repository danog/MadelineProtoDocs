---
title: contacts.getContactIDs
description: Get contact by telegram IDs
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_getContactIDs.html
---
# Method: contacts.getContactIDs
[Back to methods index](index.md)



Get contact by telegram IDs

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [int](../types/int.md) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [Vector\_of\_int](../types/int.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_int = $MadelineProto->contacts->getContactIDs(['hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
Vector_of_int = contacts.getContactIDs({hash={int}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|-503|Timeout|Timeout while fetching data|


