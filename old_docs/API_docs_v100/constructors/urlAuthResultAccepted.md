---
title: urlAuthResultAccepted
description: Details about an accepted authorization request, for more info [click here »](https://core.telegram.org/api/url-authorization)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: urlAuthResultAccepted  
[Back to constructors index](index.md)



Details about an accepted authorization request, for more info [click here »](https://core.telegram.org/api/url-authorization)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|The URL name of the website on which the user has logged in.|



### Type: [UrlAuthResult](../types/UrlAuthResult.md)


### Example:

```php
$urlAuthResultAccepted = ['_' => 'urlAuthResultAccepted', 'url' => 'string'];
```  


Or, if you're into Lua:

```lua
urlAuthResultAccepted={_='urlAuthResultAccepted', url='string'}

```


