---
title: help.termsOfService
description: help_termsOfService attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: help.termsOfService  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|popup|[Bool](../types/Bool.md) | Optional|
|id|[DataJSON](../types/DataJSON.md) | Yes|
|text|[string](../types/string.md) | Yes|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Yes|
|min\_age\_confirm|[int](../types/int.md) | Optional|



### Type: [help\_TermsOfService](../types/help_TermsOfService.md)


### Example:

```php
$help_termsOfService = ['_' => 'help.termsOfService', 'popup' => Bool, 'id' => DataJSON, 'text' => 'string', 'entities' => [MessageEntity, MessageEntity], 'min_age_confirm' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "help.termsOfService", "popup": Bool, "id": DataJSON, "text": "string", "entities": [MessageEntity], "min_age_confirm": int}
```


Or, if you're into Lua:

```lua
help_termsOfService={_='help.termsOfService', popup=Bool, id=DataJSON, text='string', entities={MessageEntity}, min_age_confirm=int}

```


