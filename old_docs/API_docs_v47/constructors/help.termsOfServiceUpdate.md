---
title: help.termsOfServiceUpdate
description: Info about an update of telegram's terms of service. If the terms of service are declined, then the [account.deleteAccount](../methods/account.deleteAccount.md) method should be called with the reason "Decline ToS update"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_termsOfServiceUpdate.html
---
# Constructor: help.termsOfServiceUpdate  
[Back to constructors index](index.md)



Info about an update of telegram's terms of service. If the terms of service are declined, then the [account.deleteAccount](../methods/account.deleteAccount.md) method should be called with the reason "Decline ToS update"

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|expires|[int](../types/int.md) | Yes|New TOS updates will have to be queried using [help.getTermsOfServiceUpdate](../methods/help.getTermsOfServiceUpdate.md) in `expires` seconds|
|terms\_of\_service|[help.TermsOfService](../constructors/help.TermsOfService.md) | Yes|New terms of service|



### Type: [help.TermsOfServiceUpdate](../types/help.TermsOfServiceUpdate.md)


### Example:

```php
$help_termsOfServiceUpdate = ['_' => 'help.termsOfServiceUpdate', 'expires' => int, 'terms_of_service' => help.TermsOfService];
```  


Or, if you're into Lua:

```lua
help_termsOfServiceUpdate={_='help.termsOfServiceUpdate', expires=int, terms_of_service=help.TermsOfService}

```


