---
title: "help.termsOfServiceUpdateEmpty"
description: "No changes were made to telegram's terms of service"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_termsOfServiceUpdateEmpty.html
---
# Constructor: help.termsOfServiceUpdateEmpty  
[Back to constructors index](index.md)



No changes were made to telegram's terms of service

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|expires|[int](../types/int.md) | Yes|New TOS updates will have to be queried using [help.getTermsOfServiceUpdate](../methods/help.getTermsOfServiceUpdate.md) in `expires` seconds|



### Type: [help.TermsOfServiceUpdate](../types/help.TermsOfServiceUpdate.md)


### Example:

```php
$help_termsOfServiceUpdateEmpty = ['_' => 'help.termsOfServiceUpdateEmpty', 'expires' => int];
```  


Or, if you're into Lua:

```lua
help_termsOfServiceUpdateEmpty={_='help.termsOfServiceUpdateEmpty', expires=int}

```


