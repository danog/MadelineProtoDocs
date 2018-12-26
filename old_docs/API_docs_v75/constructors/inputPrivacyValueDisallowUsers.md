---
title: inputPrivacyValueDisallowUsers
description: Privacy value disallow users
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPrivacyValueDisallowUsers  
[Back to constructors index](index.md)



Privacy value disallow users

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | Yes|Users|



### Type: [InputPrivacyRule](../types/InputPrivacyRule.md)


### Example:

```php
$inputPrivacyValueDisallowUsers = ['_' => 'inputPrivacyValueDisallowUsers', 'users' => [InputUser, InputUser]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputPrivacyValueDisallowUsers", "users": [InputUser]}
```


Or, if you're into Lua:

```lua
inputPrivacyValueDisallowUsers={_='inputPrivacyValueDisallowUsers', users={InputUser}}

```


