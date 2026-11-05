# messages.webPagePreview

> Represents a webpage preview.

[Back to constructors index](/API_docs/constructors/index.html)



Represents a webpage preview.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|media|[MessageMedia](/API_docs/types/MessageMedia.html) | Optional|The [messageMediaWebPage](../constructors/messageMediaWebPage.html) or a [messageMediaEmpty](../constructors/messageMediaEmpty.html) if there is no preview.|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats mentioned in the `gift` field.|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned within the `media` object.|



### Type: [messages.WebPagePreview](/API_docs/types/messages.WebPagePreview.html)


### Example:

```
$messages_webPagePreview = ['_' => 'messages.webPagePreview', 'media' => MessageMedia, 'chats' => [Chat, Chat], 'users' => [User, User]];
```
