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
|popup|[Bool](../types/Bool.md) | Optional|Whether a prompt must be showed to the user, in order to accept the new terms.|
|id|[DataJSON](../types/DataJSON.md) | Yes|ID of the new terms|
|text|[string](../types/string.md) | Yes|Text of the new terms|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Yes|Entities|
|min\_age\_confirm|[int](../types/int.md) | Optional|Minimum age required to sign up to telegram, the user must confirm that they is older than the minimum age.|



### Type: [help.wTermsOfService](../types/help.wTermsOfService.md)


### Example:

```php
$help.termsOfService = ['_' => 'help.termsOfService', 'popup' => Bool, 'id' => DataJSON, 'text' => 'string', 'entities' => [MessageEntity, MessageEntity], 'min_age_confirm' => int];
```  


Or, if you're into Lua:

```lua
help.termsOfService={_='help.termsOfService', popup=Bool, id=DataJSON, text='string', entities={MessageEntity}, min_age_confirm=int}

```


