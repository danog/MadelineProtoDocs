# messages.translateResult

> Translated text with entities

[Back to constructors index](/API_docs/constructors/index.html)



Translated text with [entities](https://core.telegram.org/api/entities)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|result|Array of [TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|Text+[entities](https://core.telegram.org/api/entities), for each input message.|



### Type: [messages.TranslatedText](/API_docs/types/messages.TranslatedText.html)


### Example:

```
$messages_translateResult = ['_' => 'messages.translateResult', 'result' => [TextWithEntities, TextWithEntities]];
```
