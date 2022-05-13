---
title: "help.termsOfService"
description: "Info about the latest telegram Terms Of Service"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_termsOfService.html
---
# Constructor: help.termsOfService  
[Back to constructors index](/API_docs/constructors/index.html)



Info about the latest telegram Terms Of Service

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|popup|[Bool](/API_docs/types/Bool.html) | Optional|Whether a prompt must be showed to the user, in order to accept the new terms.|
|id|[DataJSON](/API_docs/types/DataJSON.html) | Yes|ID of the new terms|
|text|[string](/API_docs/types/string.html) | Yes|Text of the new terms|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Yes|[Message entities for styled text](https://core.telegram.org/api/entities)|
|min\_age\_confirm|[int](/API_docs/types/int.html) | Optional|Minimum age required to sign up to telegram, the user must confirm that they is older than the minimum age.|



### Type: [help.TermsOfService](/API_docs/types/help.TermsOfService.html)


### Example:

```
$help_termsOfService = ['_' => 'help.termsOfService', 'popup' => Bool, 'id' => DataJSON, 'text' => 'string', 'entities' => [MessageEntity, MessageEntity], 'min_age_confirm' => int];
```  
