---
title: "privacyValueAllowUsers"
description: "Allow only certain users"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: privacyValueAllowUsers  
[Back to constructors index](index.md)



Allow only certain users

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [long](../types/long.md) | Yes|Allowed users|



### Type: [PrivacyRule](../types/PrivacyRule.md)


### Example:

```php
$privacyValueAllowUsers = ['_' => 'privacyValueAllowUsers', 'users' => [long, long]];
```  
