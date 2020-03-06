---
title: account.contentSettings
description: account.contentSettings attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_contentSettings.html
---
# Constructor: account.contentSettings  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|sensitive\_enabled|[Bool](../types/Bool.md) | Optional|
|sensitive\_can\_change|[Bool](../types/Bool.md) | Optional|



### Type: [account.ContentSettings](../types/account.ContentSettings.md)


### Example:

```php
$account.contentSettings = ['_' => 'account.contentSettings', 'sensitive_enabled' => Bool, 'sensitive_can_change' => Bool];
```  


Or, if you're into Lua:

```lua
account.contentSettings={_='account.contentSettings', sensitive_enabled=Bool, sensitive_can_change=Bool}

```


