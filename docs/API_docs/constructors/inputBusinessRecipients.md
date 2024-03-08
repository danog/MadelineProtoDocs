---
title: "inputBusinessRecipients"
description: "inputBusinessRecipients attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBusinessRecipients  
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



### Type: [InputBusinessRecipients](/API_docs/types/InputBusinessRecipients.html)


### Example:

```
$inputBusinessRecipients = ['_' => 'inputBusinessRecipients', 'existing_chats' => Bool, 'new_chats' => Bool, 'contacts' => Bool, 'non_contacts' => Bool, 'exclude_selected' => Bool, 'users' => [InputUser, InputUser]];
```  
