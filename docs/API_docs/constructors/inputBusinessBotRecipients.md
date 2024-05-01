---
title: "inputBusinessBotRecipients"
description: "inputBusinessBotRecipients attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBusinessBotRecipients  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|existing\_chats|[Bool](/API_docs/types/Bool.html) | Optional|
|new\_chats|[Bool](/API_docs/types/Bool.html) | Optional|
|contacts|[Bool](/API_docs/types/Bool.html) | Optional|
|non\_contacts|[Bool](/API_docs/types/Bool.html) | Optional|
|exclude\_selected|[Bool](/API_docs/types/Bool.html) | Optional|
|users|Array of [Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|
|exclude\_users|Array of [Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|



### Type: [InputBusinessBotRecipients](/API_docs/types/InputBusinessBotRecipients.html)


### Example:

```
$inputBusinessBotRecipients = ['_' => 'inputBusinessBotRecipients', 'existing_chats' => Bool, 'new_chats' => Bool, 'contacts' => Bool, 'non_contacts' => Bool, 'exclude_selected' => Bool, 'users' => [InputUser, InputUser], 'exclude_users' => [InputUser, InputUser]];
```  
