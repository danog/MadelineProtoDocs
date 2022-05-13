---
title: "securePlainEmail"
description: "Email address to use in telegram passport: it must be verified, first »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: securePlainEmail  
[Back to constructors index](/API_docs/constructors/index.html)



Email address to use in [telegram passport](https://core.telegram.org/passport): [it must be verified, first »](https://core.telegram.org/passport/encryption#secureplaindata).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|email|[string](/API_docs/types/string.html) | Yes|Email address|



### Type: [SecurePlainData](/API_docs/types/SecurePlainData.html)


### Example:

```
$securePlainEmail = ['_' => 'securePlainEmail', 'email' => 'string'];
```  
