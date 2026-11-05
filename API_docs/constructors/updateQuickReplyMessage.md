# updateQuickReplyMessage

> A new message was added to a quick reply shortcut ».

[Back to constructors index](/API_docs/constructors/index.html)



A new message was added to a [quick reply shortcut »](https://core.telegram.org/api/business#quick-reply-shortcuts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](/API_docs/types/Message.html) | Optional|The message that was added (the [message](../constructors/message.html).`quick_reply_shortcut_id` field will contain the shortcut ID).|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateQuickReplyMessage = ['_' => 'updateQuickReplyMessage', 'message' => Message];
```
