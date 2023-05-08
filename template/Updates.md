You can use the following methods to extract information from this constructor:

```php
// Extract an array of Update constructors
$vector_of_update = $MadelineProto->extractUpdates($Updates);

// Extract an updateNewMessage, updateNewChannelMessage, updateEditMessage, updateEditChannelMessage constructor
$message_update = $MadelineProto->extractMessageUpdate($Updates);

// Extract a message constructor
$message = $MadelineProto->extractMessage($Updates);

// Extract a message ID
$message = $MadelineProto->extractMessageId($Updates);
```
