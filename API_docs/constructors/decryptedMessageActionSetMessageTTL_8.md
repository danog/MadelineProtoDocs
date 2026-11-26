# decryptedMessageActionSetMessageTTL

> Setting of a message lifetime after reading.

[Back to constructors index](/API_docs/constructors/index.html)



Setting of a message lifetime after reading.

Upon receiving such message the client shall start deleting of all messages of an encrypted chat **ttl\_seconds** seconds after the messages were read by user.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|ttl\_seconds|[int](/API_docs/types/int.html) | Yes|Lifetime in seconds|



### Type: [DecryptedMessageAction](/API_docs/types/DecryptedMessageAction.html)


### Example:

```
$decryptedMessageActionSetMessageTTL_8 = ['_' => 'decryptedMessageActionSetMessageTTL', 'ttl_seconds' => int];
```
