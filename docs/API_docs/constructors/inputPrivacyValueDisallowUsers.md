---
title: "inputPrivacyValueDisallowUsers"
description: "Disallow only certain users"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPrivacyValueDisallowUsers  
[Back to constructors index](/API_docs/constructors/index.html)



Disallow only certain users

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Yes|Users to disallow|



### Type: [InputPrivacyRule](/API_docs/types/InputPrivacyRule.html)


### Example:

```
$inputPrivacyValueDisallowUsers = ['_' => 'inputPrivacyValueDisallowUsers', 'users' => [InputUser, InputUser]];
```  
