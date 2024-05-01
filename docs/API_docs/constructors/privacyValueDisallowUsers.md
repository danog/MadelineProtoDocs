---
title: "privacyValueDisallowUsers"
description: "Disallow only certain users"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: privacyValueDisallowUsers  
[Back to constructors index](/API_docs/constructors/index.html)



Disallow only certain users

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [long](/API_docs/types/long.html) | Yes|Disallowed users|



### Type: [PrivacyRule](/API_docs/types/PrivacyRule.html)


### Example:

```
$privacyValueDisallowUsers = ['_' => 'privacyValueDisallowUsers', 'users' => [long, long]];
```  
