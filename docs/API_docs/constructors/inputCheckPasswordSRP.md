---
title: "inputCheckPasswordSRP"
description: "Constructor for checking the validity of a 2FA SRP password (see SRP)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputCheckPasswordSRP  
[Back to constructors index](/API_docs/constructors/index.html)



Constructor for checking the validity of a 2FA SRP password (see [SRP](https://core.telegram.org/api/srp))

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|srp\_id|[long](/API_docs/types/long.html) | Yes|[SRP ID](https://core.telegram.org/api/srp)|
|A|[bytes](/API_docs/types/bytes.html) | Yes|`A` parameter (see [SRP](https://core.telegram.org/api/srp))|
|M1|[bytes](/API_docs/types/bytes.html) | Yes|`M1` parameter (see [SRP](https://core.telegram.org/api/srp))|



### Type: [InputCheckPasswordSRP](/API_docs/types/InputCheckPasswordSRP.html)


### Example:

```
$inputCheckPasswordSRP = ['_' => 'inputCheckPasswordSRP', 'srp_id' => long, 'A' => 'bytes', 'M1' => 'bytes'];
```  
