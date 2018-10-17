---
title: privacyValueDisallowUsers
description: privacyValueDisallowUsers attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: privacyValueDisallowUsers  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|users|Array of [int](../types/int.md) | Yes|



### Type: [PrivacyRule](../types/PrivacyRule.md)


### Example:

```php
$privacyValueDisallowUsers = ['_' => 'privacyValueDisallowUsers', 'users' => [int, int]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "privacyValueDisallowUsers", "users": [int]}
```


Or, if you're into Lua:

```lua
privacyValueDisallowUsers={_='privacyValueDisallowUsers', users={int}}

```


