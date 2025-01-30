---
title: "inputBusinessRecipients"
description: "Specifies the chats that can receive Telegram Business away » and greeting » messages."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBusinessRecipients  
[Back to constructors index](/API_docs/constructors/index.html)



Specifies the chats that **can** receive Telegram Business [away »](https://core.telegram.org/api/business#away-messages) and [greeting »](https://core.telegram.org/api/business#greeting-messages) messages.

If `exclude_selected` is set, specifies all chats that **cannot** receive Telegram Business [away »](https://core.telegram.org/api/business#away-messages) and [greeting »](https://core.telegram.org/api/business#greeting-messages) messages.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|existing\_chats|[Bool](/API_docs/types/Bool.html) | Optional|All existing private chats.|
|new\_chats|[Bool](/API_docs/types/Bool.html) | Optional|All new private chats.|
|contacts|[Bool](/API_docs/types/Bool.html) | Optional|All private chats with contacts.|
|non\_contacts|[Bool](/API_docs/types/Bool.html) | Optional|All private chats with non-contacts.|
|exclude\_selected|[Bool](/API_docs/types/Bool.html) | Optional|If set, inverts the selection.|
|users|Array of [Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|Only private chats with the specified users.|



### Type: [InputBusinessRecipients](/API_docs/types/InputBusinessRecipients.html)


### Example:

```
$inputBusinessRecipients = ['_' => 'inputBusinessRecipients', 'existing_chats' => Bool, 'new_chats' => Bool, 'contacts' => Bool, 'non_contacts' => Bool, 'exclude_selected' => Bool, 'users' => [InputUser, InputUser]];
```  
