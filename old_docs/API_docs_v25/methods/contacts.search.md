---
title: contacts.search
description: Returns users found by username substring.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_search.html
---
# Method: contacts.search
[Back to methods index](index.md)



Returns users found by username substring.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|q|[string](../types/string.md) | Target substring | Yes|
|limit|[int](../types/int.md) | Maximum number of users to be returned | Yes|


### Return type: [contacts.Found](../types/contacts.Found.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$contacts.Found = $MadelineProto->contacts->search(['q' => 'string', 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
contacts.Found = contacts.search({q='string', limit=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|QUERY_TOO_SHORT|The query string is too short|
|400|SEARCH_QUERY_EMPTY|The search query is empty|
|-503|Timeout|Timeout while fetching data|


