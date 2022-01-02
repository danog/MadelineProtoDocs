---
title: "accountDaysTTL"
description: "Time to live in days of the current account"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: accountDaysTTL  
[Back to constructors index](index.md)



Time to live in days of the current account

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|days|[int](../types/int.md) | Yes|This account will self-destruct in the specified number of days|



### Type: [AccountDaysTTL](../types/AccountDaysTTL.md)


### Example:

```php
$accountDaysTTL = ['_' => 'accountDaysTTL', 'days' => int];
```  


Or, if you're into Lua:

```lua
accountDaysTTL={_='accountDaysTTL', days=int}

```


