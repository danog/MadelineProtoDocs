# encryptedMessageService

> Encrypted service message

[Back to constructors index](/API_docs/constructors/index.html)



Encrypted service message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](/API_docs/types/int.html) | Yes|ID of encrypted chat|
|date|[int](/API_docs/types/int.html) | Yes|Date of sending|
|decrypted\_message|[DecryptedMessage](/API_docs/types/DecryptedMessage.html) | Yes|



### Type: [EncryptedMessage](/API_docs/types/EncryptedMessage.html)


### Example:

```
$encryptedMessageService = ['_' => 'encryptedMessageService', 'chat_id' => int, 'date' => int, 'decrypted_message' => DecryptedMessage];
```
