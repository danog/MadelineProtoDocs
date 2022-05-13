---
title: "messageMediaContact"
description: "Attached contact."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaContact  
[Back to constructors index](/API_docs/constructors/index.html)



Attached contact.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_number|[string](/API_docs/types/string.html) | Yes|Phone number|
|first\_name|[string](/API_docs/types/string.html) | Yes|Contact's first name|
|last\_name|[string](/API_docs/types/string.html) | Yes|Contact's last name|
|vcard|[string](/API_docs/types/string.html) | Yes|VCARD of contact|
|user\_id|[long](/API_docs/types/long.html) | Yes|User identifier or `0`, if the user with the given phone number is not registered|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaContact = ['_' => 'messageMediaContact', 'phone_number' => 'string', 'first_name' => 'string', 'last_name' => 'string', 'vcard' => 'string', 'user_id' => long];
```  
