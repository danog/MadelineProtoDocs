---
title: "inputBusinessBotRecipients"
description: "Specifies the private chats that a connected business bot » may interact with."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBusinessBotRecipients  
[Back to constructors index](/API_docs/constructors/index.html)



Specifies the private chats that a [connected business bot »](https://core.telegram.org/api/bots/connected-business-bots) may interact with.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|existing\_chats|[Bool](/API_docs/types/Bool.html) | Optional|Selects all existing private chats.|
|new\_chats|[Bool](/API_docs/types/Bool.html) | Optional|Selects all new private chats.|
|contacts|[Bool](/API_docs/types/Bool.html) | Optional|Selects all private chats with contacts.|
|non\_contacts|[Bool](/API_docs/types/Bool.html) | Optional|Selects all private chats with non-contacts.|
|exclude\_selected|[Bool](/API_docs/types/Bool.html) | Optional|If set, then all private chats *except* the ones selected by `existing_chats`, `new_chats`, `contacts`, `non_contacts` and `users` are chosen. <br>Note that if this flag is set, any values passed in `exclude_users` will be merged and moved into `users` by the server.|
|users|Array of [Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|Explicitly selected private chats.|
|exclude\_users|Array of [Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|Identifiers of private chats that are always excluded.|



### Type: [InputBusinessBotRecipients](/API_docs/types/InputBusinessBotRecipients.html)


### Example:

```
$inputBusinessBotRecipients = ['_' => 'inputBusinessBotRecipients', 'existing_chats' => Bool, 'new_chats' => Bool, 'contacts' => Bool, 'non_contacts' => Bool, 'exclude_selected' => Bool, 'users' => [InputUser, InputUser], 'exclude_users' => [InputUser, InputUser]];
```  
