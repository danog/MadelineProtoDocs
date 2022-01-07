---
title: "privacyValueDisallowUsers"
description: "Disallow only certain users"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: privacyValueDisallowUsers  
[Back to constructors index](index.md)



Disallow only certain users

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [long](../types/long.md) | Yes|Disallowed users|



### Type: [PrivacyRule](../types/PrivacyRule.md)


### Example:

```php
$privacyValueDisallowUsers = ['_' => 'privacyValueDisallowUsers', 'users' => [long, long]];
```  
