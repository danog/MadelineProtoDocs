# messages.stickerSetInstallResultArchive

> The stickerset was installed, but since there are too many stickersets some were archived

[Back to constructors index](/API_docs/constructors/index.html)



The stickerset was installed, but since there are too many stickersets some were archived

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|sets|Array of [StickerSetCovered](/API_docs/types/StickerSetCovered.html) | Yes|Archived stickersets|



### Type: [messages.StickerSetInstallResult](/API_docs/types/messages.StickerSetInstallResult.html)


### Example:

```
$messages_stickerSetInstallResultArchive = ['_' => 'messages.stickerSetInstallResultArchive', 'sets' => [StickerSetCovered, StickerSetCovered]];
```
