---
title: privacyValueAllowUsers
description: Allow only certain users
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: privacyValueAllowUsers  
[Back to constructors index](index.md)



Allow only certain users

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [int](../types/int.md) | Yes|Allowed users|



### Type: [PrivacyRule](../types/PrivacyRule.md)


### Example:

```php
$privacyValueAllowUsers = ['_' => 'privacyValueAllowUsers', 'users' => [int, int]];
```  


Or, if you're into Lua:

```lua
privacyValueAllowUsers={_='privacyValueAllowUsers', users={int}}

```


