---
title: "secureValueHash"
description: "Secure value hash"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueHash  
[Back to constructors index](/API_docs/constructors/index.md)



Secure value hash

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](/API_docs/types/SecureValueType.md) | Yes|Secure value type|
|hash|[bytes](/API_docs/types/bytes.md) | Yes|Hash|



### Type: [SecureValueHash](/API_docs/types/SecureValueHash.md)


### Example:

```php
$secureValueHash = ['_' => 'secureValueHash', 'type' => SecureValueType, 'hash' => 'bytes'];
```  
