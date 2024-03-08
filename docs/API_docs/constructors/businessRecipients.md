---
title: "businessRecipients"
description: "businessRecipients attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: businessRecipients  
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



### Type: [BusinessRecipients](/API_docs/types/BusinessRecipients.html)


### Example:

```
$businessRecipients = ['_' => 'businessRecipients', 'existing_chats' => Bool, 'new_chats' => Bool, 'contacts' => Bool, 'non_contacts' => Bool, 'exclude_selected' => Bool, 'users' => [long, long]];
```  
