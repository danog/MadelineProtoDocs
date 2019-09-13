---
title: urlAuthResultRequest
description: Request
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: urlAuthResultRequest  
[Back to constructors index](index.md)



Request

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|request\_write\_access|[Bool](../types/Bool.md) | Optional|Request write access?|
|bot|[User](../types/User.md) | Optional|Bot|
|domain|[string](../types/string.md) | Yes|Doamin|



### Type: [UrlAuthResult](../types/UrlAuthResult.md)


### Example:

```php
$urlAuthResultRequest = ['_' => 'urlAuthResultRequest', 'request_write_access' => Bool, 'bot' => User, 'domain' => 'string'];
```  


Or, if you're into Lua:

```lua
urlAuthResultRequest={_='urlAuthResultRequest', request_write_access=Bool, bot=User, domain='string'}

```


