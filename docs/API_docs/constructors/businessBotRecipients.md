---
title: "businessBotRecipients"
description: "Specifies the private chats that a connected business bot » may receive messages and interact with."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: businessBotRecipients  
[Back to constructors index](/API_docs/constructors/index.html)



Specifies the private chats that a [connected business bot »](https://core.telegram.org/api/bots/connected-business-bots) may receive messages and interact with.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|existing\_chats|[Bool](/API_docs/types/Bool.html) | Optional|Selects all existing private chats.|
|new\_chats|[Bool](/API_docs/types/Bool.html) | Optional|Selects all new private chats.|
|contacts|[Bool](/API_docs/types/Bool.html) | Optional|Selects all private chats with contacts.|
|non\_contacts|[Bool](/API_docs/types/Bool.html) | Optional|Selects all private chats with non-contacts.|
|exclude\_selected|[Bool](/API_docs/types/Bool.html) | Optional|If set, then all private chats *except* the ones selected by `existing_chats`, `new_chats`, `contacts`, `non_contacts` and `users` are chosen. <br>Note that if this flag is set, any values passed in `exclude_users` will be merged and moved into `users` by the server, thus `exclude_users` will always be empty.|
|users|Array of [long](/API_docs/types/long.html) | Optional|Explicitly selected private chats.|
|exclude\_users|Array of [long](/API_docs/types/long.html) | Optional|Identifiers of private chats that are always excluded.|



### Type: [BusinessBotRecipients](/API_docs/types/BusinessBotRecipients.html)


### Example:

```
$businessBotRecipients = ['_' => 'businessBotRecipients', 'existing_chats' => Bool, 'new_chats' => Bool, 'contacts' => Bool, 'non_contacts' => Bool, 'exclude_selected' => Bool, 'users' => [long, long], 'exclude_users' => [long, long]];
```  
