# updateEncryption

> Change of state in an encrypted chat.

[Back to constructors index](/API_docs/constructors/index.html)



Change of state in an encrypted chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat|[EncryptedChat](/API_docs/types/EncryptedChat.html) | Optional|Encrypted chat|
|date|[int](/API_docs/types/int.html) | Yes|Date of change|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateEncryption = ['_' => 'updateEncryption', 'chat' => EncryptedChat, 'date' => int];
```
