# decryptedMessageMediaContact

> Contact attached to an encrypted message.

[Back to constructors index](/API_docs/constructors/index.html)



Contact attached to an encrypted message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_number|[string](/API_docs/types/string.html) | Yes|Phone number|
|first\_name|[string](/API_docs/types/string.html) | Yes|Contact's first name|
|last\_name|[string](/API_docs/types/string.html) | Yes|Contact's last name|
|user\_id|[int](/API_docs/types/int.html) | Yes|Telegram User ID of signed-up contact|



### Type: [DecryptedMessageMedia](/API_docs/types/DecryptedMessageMedia.html)


### Example:

```
$decryptedMessageMediaContact_8 = ['_' => 'decryptedMessageMediaContact', 'phone_number' => 'string', 'first_name' => 'string', 'last_name' => 'string', 'user_id' => int];
```
