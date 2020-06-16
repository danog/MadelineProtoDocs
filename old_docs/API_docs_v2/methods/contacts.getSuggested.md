---
title: contacts.getSuggested
description: contacts.getSuggested parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_getSuggested.html
---
# Method: contacts.getSuggested
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|limit|[int](../types/int.md) | Yes|


### Return type: [contacts.Suggested](../types/contacts.Suggested.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$contacts.Suggested = $MadelineProto->contacts->getSuggested(['limit' => int, ]);
```

Or, if you're into Lua:

```lua
contacts.Suggested = contacts.getSuggested({limit=int, })
```

