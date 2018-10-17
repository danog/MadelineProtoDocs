---
title: help.termsOfServiceUpdate
description: help_termsOfServiceUpdate attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: help.termsOfServiceUpdate  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|expires|[int](../types/int.md) | Yes|
|terms\_of\_service|[help\_TermsOfService](../types/help_TermsOfService.md) | Yes|



### Type: [help\_TermsOfServiceUpdate](../types/help_TermsOfServiceUpdate.md)


### Example:

```php
$help_termsOfServiceUpdate = ['_' => 'help.termsOfServiceUpdate', 'expires' => int, 'terms_of_service' => help_TermsOfService];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "help.termsOfServiceUpdate", "expires": int, "terms_of_service": help_TermsOfService}
```


Or, if you're into Lua:

```lua
help_termsOfServiceUpdate={_='help.termsOfServiceUpdate', expires=int, terms_of_service=help_TermsOfService}

```


