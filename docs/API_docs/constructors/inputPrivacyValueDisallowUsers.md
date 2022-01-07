---
title: "inputPrivacyValueDisallowUsers"
description: "Disallow only certain users"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPrivacyValueDisallowUsers  
[Back to constructors index](index.md)



Disallow only certain users

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | Yes|Users to disallow|



### Type: [InputPrivacyRule](../types/InputPrivacyRule.md)


### Example:

```php
$inputPrivacyValueDisallowUsers = ['_' => 'inputPrivacyValueDisallowUsers', 'users' => [InputUser, InputUser]];
```  
