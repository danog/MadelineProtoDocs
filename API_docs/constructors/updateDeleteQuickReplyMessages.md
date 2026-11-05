# updateDeleteQuickReplyMessages

> One or more messages in a quick reply shortcut » were deleted.

[Back to constructors index](/API_docs/constructors/index.html)



One or more messages in a [quick reply shortcut »](https://core.telegram.org/api/business#quick-reply-shortcuts) were deleted.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|shortcut\_id|[int](/API_docs/types/int.html) | Yes|Quick reply shortcut ID.|
|messages|Array of [int](/API_docs/types/int.html) | Yes|IDs of the deleted messages.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateDeleteQuickReplyMessages = ['_' => 'updateDeleteQuickReplyMessages', 'shortcut_id' => int, 'messages' => [int, int]];
```
