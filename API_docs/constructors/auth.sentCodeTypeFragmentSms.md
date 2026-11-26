# auth.sentCodeTypeFragmentSms

> The code was delivered via fragment.com.

[Back to constructors index](/API_docs/constructors/index.html)



The code was delivered via [fragment.com](https://fragment.com).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.html) | Yes|Open the specified URL to log into [fragment.com](https://fragment.com) with the wallet that owns the specified phone number and view the code.|
|length|[int](/API_docs/types/int.html) | Yes|Length of the delivered code.|



### Type: [auth.SentCodeType](/API_docs/types/auth.SentCodeType.html)


### Example:

```
$auth_sentCodeTypeFragmentSms = ['_' => 'auth.sentCodeTypeFragmentSms', 'url' => 'string', 'length' => int];
```
