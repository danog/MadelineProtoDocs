# auth.sentCodeTypeSetUpEmailRequired

> The user should add and verify an email address in order to login as described here ».

[Back to constructors index](/API_docs/constructors/index.html)



The user should add and verify an email address in order to login as described [here »](https://core.telegram.org/api/auth#email-verification).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|apple\_signin\_allowed|[Bool](/API_docs/types/Bool.html) | Optional|Whether authorization through Apple ID is allowed|
|google\_signin\_allowed|[Bool](/API_docs/types/Bool.html) | Optional|Whether authorization through Google ID is allowed|



### Type: [auth.SentCodeType](/API_docs/types/auth.SentCodeType.html)


### Example:

```
$auth_sentCodeTypeSetUpEmailRequired = ['_' => 'auth.sentCodeTypeSetUpEmailRequired', 'apple_signin_allowed' => Bool, 'google_signin_allowed' => Bool];
```
