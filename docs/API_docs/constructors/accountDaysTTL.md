---
title: "accountDaysTTL"
description: "Time to live in days of the current account"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: accountDaysTTL  
[Back to constructors index](/API_docs/constructors/index.md)



Time to live in days of the current account

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|days|[int](/API_docs/types/int.md) | Yes|This account will self-destruct in the specified number of days|



### Type: [AccountDaysTTL](/API_docs/types/AccountDaysTTL.md)


### Example:

```php
$accountDaysTTL = ['_' => 'accountDaysTTL', 'days' => int];
```  
