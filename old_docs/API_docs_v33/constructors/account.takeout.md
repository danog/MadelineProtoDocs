---
title: account.takeout
description: Takout info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_takeout.html
---
# Constructor: account.takeout  
[Back to constructors index](index.md)



Takout info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Takeout ID|



### Type: [account.Takeout](../types/account.Takeout.md)


### Example:

```php
$account.takeout = ['_' => 'account.takeout', 'id' => long];
```  


Or, if you're into Lua:

```lua
account.takeout={_='account.takeout', id=long}

```


