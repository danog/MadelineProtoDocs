# bots.previewInfo

> Contains info about Main Mini App previews, see here » for more info.

[Back to constructors index](/API_docs/constructors/index.html)



Contains info about [Main Mini App previews, see here »](https://core.telegram.org/api/bots/webapps#main-mini-app-previews) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|media|Array of [BotPreviewMedia](/API_docs/types/BotPreviewMedia.html) | Yes|All preview medias for the language code passed to [bots.getPreviewInfo](../methods/bots.getPreviewInfo.html).|
|lang\_codes|Array of [string](/API_docs/types/string.html) | Yes|All available language codes for which preview medias were uploaded (regardless of the language code passed to [bots.getPreviewInfo](../methods/bots.getPreviewInfo.html)).|



### Type: [bots.PreviewInfo](/API_docs/types/bots.PreviewInfo.html)


### Example:

```
$bots_previewInfo = ['_' => 'bots.previewInfo', 'media' => [BotPreviewMedia, BotPreviewMedia], 'lang_codes' => ['string', 'string']];
```
