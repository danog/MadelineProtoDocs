---
title: contacts.deleteByPhones
description: Delete contacts by phone number
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.deleteByPhones  
[Back to methods index](index.md)


Delete contacts by phone number

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phones|Array of [string](../types/string.md) | Phones | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->contacts->deleteByPhones(['phones' => ['string', 'string'], ]);
```

Or, if you're into Lua:

```lua
Bool = contacts.deleteByPhones({phones={'string'}, })
```

