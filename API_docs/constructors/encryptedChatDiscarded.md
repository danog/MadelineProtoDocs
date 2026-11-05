# encryptedChatDiscarded

> Discarded or deleted chat.

[Back to constructors index](/API_docs/constructors/index.html)



Discarded or deleted chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|history\_deleted|[Bool](/API_docs/types/Bool.html) | Optional|Whether both users of this secret chat should also remove all of its messages|
|id|[int](/API_docs/types/int.html) | Yes|Chat ID|



### Type: [EncryptedChat](/API_docs/types/EncryptedChat.html)


### Example:

```
$encryptedChatDiscarded = ['_' => 'encryptedChatDiscarded', 'history_deleted' => Bool, 'id' => int];
```
