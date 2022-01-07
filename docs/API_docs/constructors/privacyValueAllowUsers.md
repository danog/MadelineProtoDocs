---
title: "privacyValueAllowUsers"
description: "Allow only certain users"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: privacyValueAllowUsers  
[Back to constructors index](/API_docs/constructors/index.md)



Allow only certain users

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [long](/API_docs/types/long.md) | Yes|Allowed users|



### Type: [PrivacyRule](/API_docs/types/PrivacyRule.md)


### Example:

```php
$privacyValueAllowUsers = ['_' => 'privacyValueAllowUsers', 'users' => [long, long]];
```  
