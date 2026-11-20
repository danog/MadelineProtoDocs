# auth.sentCodeTypeCall

> The code will be sent via a phone call: a synthesized voice will tell the user which verification code to input.

[Back to constructors index](/API_docs/constructors/index.html)



The code will be sent via a phone call: a synthesized voice will tell the user which verification code to input.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|length|[int](/API_docs/types/int.html) | Yes|Length of the verification code|



### Type: [auth.SentCodeType](/API_docs/types/auth.SentCodeType.html)


### Example:

```
$auth_sentCodeTypeCall = ['_' => 'auth.sentCodeTypeCall', 'length' => int];
```
