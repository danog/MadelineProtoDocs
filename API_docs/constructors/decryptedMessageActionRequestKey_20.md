# decryptedMessageActionRequestKey

> Request rekeying, see rekeying process

[Back to constructors index](/API_docs/constructors/index.html)



Request rekeying, see [rekeying process](https://core.telegram.org/api/end-to-end/pfs)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|exchange\_id|[long](/API_docs/types/long.html) | Yes|Exchange ID|
|g\_a|[bytes](/API_docs/types/bytes.html) | Yes|g\_a, see [rekeying process](https://core.telegram.org/api/end-to-end/pfs)|



### Type: [DecryptedMessageAction](/API_docs/types/DecryptedMessageAction.html)


### Example:

```
$decryptedMessageActionRequestKey_20 = ['_' => 'decryptedMessageActionRequestKey', 'exchange_id' => long, 'g_a' => 'bytes'];
```
