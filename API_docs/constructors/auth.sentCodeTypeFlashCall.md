# auth.sentCodeTypeFlashCall

> The code will be sent via a flash phone call, that will be closed immediately. The phone code will then be the phone number itself, just make sure that the phone number matches the specified pattern.

[Back to constructors index](/API_docs/constructors/index.html)



The code will be sent via a flash phone call, that will be closed immediately. The phone code will then be the phone number itself, just make sure that the phone number matches the specified pattern.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pattern|[string](/API_docs/types/string.html) | Yes|[pattern](https://core.telegram.org/api/pattern) to match|



### Type: [auth.SentCodeType](/API_docs/types/auth.SentCodeType.html)


### Example:

```
$auth_sentCodeTypeFlashCall = ['_' => 'auth.sentCodeTypeFlashCall', 'pattern' => 'string'];
```
