---
title: "inputPrivacyValueAllowUsers"
description: "Allow only certain users"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPrivacyValueAllowUsers  
[Back to constructors index](/API_docs/constructors/index.md)



Allow only certain users

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.md) | Yes|Allowed users|



### Type: [InputPrivacyRule](/API_docs/types/InputPrivacyRule.md)


### Example:

```php
$inputPrivacyValueAllowUsers = ['_' => 'inputPrivacyValueAllowUsers', 'users' => [InputUser, InputUser]];
```  
