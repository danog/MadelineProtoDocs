---
title: "securePlainPhone"
description: "Phone number to use in telegram passport: it must be verified, first »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: securePlainPhone  
[Back to constructors index](/API_docs/constructors/index.html)



Phone number to use in [telegram passport](https://core.telegram.org/passport): [it must be verified, first »](https://core.telegram.org/passport/encryption#secureplaindata).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone|[string](/API_docs/types/string.html) | Yes|Phone number|



### Type: [SecurePlainData](/API_docs/types/SecurePlainData.html)


### Example:

```
$securePlainPhone = ['_' => 'securePlainPhone', 'phone' => 'string'];
```  
