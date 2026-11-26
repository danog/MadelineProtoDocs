# phone.phoneCall

> A VoIP phone call

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
