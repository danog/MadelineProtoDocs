# decryptedMessageActionAcceptKey

> Accept new key

[Back to constructors index](/API_docs/constructors/index.html)



Accept new key

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|exchange\_id|[long](/API_docs/types/long.html) | Yes|Exchange ID|
|g\_b|[bytes](/API_docs/types/bytes.html) | Yes|B parameter, see [rekeying process](https://core.telegram.org/api/end-to-end/pfs)|
|key\_fingerprint|[long](/API_docs/types/long.html) | Yes|Key fingerprint, see [rekeying process](https://core.telegram.org/api/end-to-end/pfs)|



### Type: [DecryptedMessageAction](/API_docs/types/DecryptedMessageAction.html)


### Example:

```
$decryptedMessageActionAcceptKey_20 = ['_' => 'decryptedMessageActionAcceptKey', 'exchange_id' => long, 'g_b' => 'bytes', 'key_fingerprint' => long];
```
