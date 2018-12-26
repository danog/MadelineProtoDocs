---
title: help.termsOfService
description: Terms of service
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: help.termsOfService  
[Back to constructors index](index.md)



Terms of service

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|popup|[Bool](../types/Bool.md) | Optional|Popup?|
|id|[DataJSON](../types/DataJSON.md) | Yes|ID|
|text|[string](../types/string.md) | Yes|Text|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Yes|Entities|
|min\_age\_confirm|[int](../types/int.md) | Optional|Min age confirm|



### Type: [help\_wTermsOfService](../types/help_wTermsOfService.md)


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


