# updateSentPhoneCode

> A paid login SMS code was successfully sent.

[Back to constructors index](/API_docs/constructors/index.html)



A paid login SMS code was successfully sent.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|sent\_code|[auth.SentCode](/API_docs/constructors/auth.SentCode.html) | Yes|Info about the sent code.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateSentPhoneCode = ['_' => 'updateSentPhoneCode', 'sent_code' => auth.SentCode];
```
