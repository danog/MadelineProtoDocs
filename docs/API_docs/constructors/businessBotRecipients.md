---
title: "businessBotRecipients"
description: "businessBotRecipients attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: businessBotRecipients  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|existing\_chats|[Bool](/API_docs/types/Bool.html) | Optional|
|new\_chats|[Bool](/API_docs/types/Bool.html) | Optional|
|contacts|[Bool](/API_docs/types/Bool.html) | Optional|
|non\_contacts|[Bool](/API_docs/types/Bool.html) | Optional|
|exclude\_selected|[Bool](/API_docs/types/Bool.html) | Optional|
|users|Array of [long](/API_docs/types/long.html) | Optional|
|exclude\_users|Array of [long](/API_docs/types/long.html) | Optional|



### Type: [BusinessBotRecipients](/API_docs/types/BusinessBotRecipients.html)


### Example:

```
$businessBotRecipients = ['_' => 'businessBotRecipients', 'existing_chats' => Bool, 'new_chats' => Bool, 'contacts' => Bool, 'non_contacts' => Bool, 'exclude_selected' => Bool, 'users' => [long, long], 'exclude_users' => [long, long]];
```  
