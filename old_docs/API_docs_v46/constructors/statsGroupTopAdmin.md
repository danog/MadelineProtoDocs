---
title: statsGroupTopAdmin
description: statsGroupTopAdmin attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: statsGroupTopAdmin  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[int](../types/int.md) | Yes|
|deleted|[int](../types/int.md) | Yes|
|kicked|[int](../types/int.md) | Yes|
|banned|[int](../types/int.md) | Yes|



### Type: [StatsGroupTopAdmin](../types/StatsGroupTopAdmin.md)


### Example:

```php
$statsGroupTopAdmin = ['_' => 'statsGroupTopAdmin', 'user_id' => int, 'deleted' => int, 'kicked' => int, 'banned' => int];
```  


Or, if you're into Lua:

```lua
statsGroupTopAdmin={_='statsGroupTopAdmin', user_id=int, deleted=int, kicked=int, banned=int}

```


