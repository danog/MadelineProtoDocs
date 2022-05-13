---
title: "phone.phoneCall"
description: "A VoIP phone call"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/phone_phoneCall.html
---
# Constructor: phone.phoneCall  
[Back to constructors index](/API_docs/constructors/index.html)



A VoIP phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_call|[PhoneCall](/API_docs/types/PhoneCall.html) | Optional|The VoIP phone call|
|users|Array of [User](/API_docs/types/User.html) | Yes|VoIP phone call participants|



### Type: [phone.PhoneCall](/API_docs/types/phone.PhoneCall.html)


### Example:

```
$phone_phoneCall = ['_' => 'phone.phoneCall', 'phone_call' => PhoneCall, 'users' => [User, User]];
```  
