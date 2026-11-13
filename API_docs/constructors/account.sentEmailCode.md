# account.sentEmailCode

> The sent email code

[Back to constructors index](/API_docs/constructors/index.html)



The sent email code

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|email\_pattern|[string](/API_docs/types/string.html) | Yes|The email (to which the code was sent) must match this [pattern](https://core.telegram.org/api/pattern)|
|length|[int](/API_docs/types/int.html) | Yes|The length of the verification code|



### Type: [account.SentEmailCode](/API_docs/types/account.SentEmailCode.html)


### Example:

```
$account_sentEmailCode = ['_' => 'account.sentEmailCode', 'email_pattern' => 'string', 'length' => int];
```
