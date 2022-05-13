---
title: "privacyValueAllowUsers"
description: "Allow only certain users"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: privacyValueAllowUsers  
[Back to constructors index](/API_docs/constructors/index.html)



Allow only certain users

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [long](/API_docs/types/long.html) | Yes|Allowed users|



### Type: [PrivacyRule](/API_docs/types/PrivacyRule.html)


### Example:

```
$privacyValueAllowUsers = ['_' => 'privacyValueAllowUsers', 'users' => [long, long]];
```  
