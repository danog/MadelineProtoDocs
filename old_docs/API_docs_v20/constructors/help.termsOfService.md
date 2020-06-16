---
title: help.termsOfService
description: Info about the latest telegram Terms Of Service
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_termsOfService.html
---
# Constructor: help.termsOfService  
[Back to constructors index](index.md)



Info about the latest telegram Terms Of Service

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](../types/string.md) | Yes|Text of the new terms|



### Type: [help.TermsOfService](../types/help.TermsOfService.md)


### Example:

```php
$help.termsOfService = ['_' => 'help.termsOfService', 'text' => 'string'];
```  


Or, if you're into Lua:

```lua
help.termsOfService={_='help.termsOfService', text='string'}

```


