---
title: "inputPrivacyValueAllowUsers"
description: "Allow only certain users"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPrivacyValueAllowUsers  
[Back to constructors index](index.md)



Allow only certain users

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | Yes|Allowed users|



### Type: [InputPrivacyRule](../types/InputPrivacyRule.md)


### Example:

```php
$inputPrivacyValueAllowUsers = ['_' => 'inputPrivacyValueAllowUsers', 'users' => [InputUser, InputUser]];
```  


Or, if you're into Lua:

```lua
inputPrivacyValueAllowUsers={_='inputPrivacyValueAllowUsers', users={InputUser}}

```


