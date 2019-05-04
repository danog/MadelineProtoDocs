---
title: contacts.deleteByPhones
description: Delete contacts by phones
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.deleteByPhones  
[Back to methods index](index.md)


Delete contacts by phones

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phones|Array of [string](../types/string.md) | Phones | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->contacts->deleteByPhones(['phones' => ['string', 'string'], ]);
```

Or, if you're into Lua:

```lua
Bool = contacts.deleteByPhones({phones={'string'}, })
```

