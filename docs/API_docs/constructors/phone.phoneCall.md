---
title: "phone.phoneCall"
description: "A VoIP phone call"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/phone_phoneCall.html
---
# Constructor: phone.phoneCall  
[Back to constructors index](/API_docs/constructors/index.md)



A VoIP phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_call|[PhoneCall](/API_docs/types/PhoneCall.md) | Optional|The VoIP phone call|
|users|Array of [User](/API_docs/types/User.md) | Yes|VoIP phone call participants|



### Type: [phone.PhoneCall](/API_docs/types/phone.PhoneCall.md)


### Example:

```php
$phone_phoneCall = ['_' => 'phone.phoneCall', 'phone_call' => PhoneCall, 'users' => [User, User]];
```  
