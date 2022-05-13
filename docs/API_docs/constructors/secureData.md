---
title: "secureData"
description: "Secure passport data, for more info see the passport docs »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureData  
[Back to constructors index](/API_docs/constructors/index.html)



Secure [passport](https://core.telegram.org/passport) data, for more info [see the passport docs »](https://core.telegram.org/passport/encryption#securedata)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|data|[bytes](/API_docs/types/bytes.html) | Yes|Data|
|data\_hash|[bytes](/API_docs/types/bytes.html) | Yes|Data hash|
|secret|[bytes](/API_docs/types/bytes.html) | Yes|Secret|



### Type: [SecureData](/API_docs/types/SecureData.html)


### Example:

```
$secureData = ['_' => 'secureData', 'data' => 'bytes', 'data_hash' => 'bytes', 'secret' => 'bytes'];
```  
