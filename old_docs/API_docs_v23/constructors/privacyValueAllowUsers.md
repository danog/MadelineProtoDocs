---
title: privacyValueAllowUsers
description: Privacy value allow users
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: privacyValueAllowUsers  
[Back to constructors index](index.md)



Privacy value allow users

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [int](../types/int.md) | Yes|Users|



### Type: [PrivacyRule](../types/PrivacyRule.md)


### Example:

```php
$privacyValueAllowUsers = ['_' => 'privacyValueAllowUsers', 'users' => [int, int]];
```  


Or, if you're into Lua:

```lua
privacyValueAllowUsers={_='privacyValueAllowUsers', users={int}}

```


