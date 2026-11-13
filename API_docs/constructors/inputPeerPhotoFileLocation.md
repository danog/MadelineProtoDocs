# inputPeerPhotoFileLocation

> Location of profile photo of channel/group/supergroup/user

[Back to constructors index](/API_docs/constructors/index.html)



Location of profile photo of channel/group/supergroup/user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|big|[Bool](/API_docs/types/Bool.html) | Optional|Whether to download the high-quality version of the picture|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|The peer whose profile picture should be downloaded|
|photo\_id|[long](/API_docs/types/long.html) | Yes|Photo ID|



### Type: [InputFileLocation](/API_docs/types/InputFileLocation.html)


### Example:

```
$inputPeerPhotoFileLocation = ['_' => 'inputPeerPhotoFileLocation', 'big' => Bool, 'peer' => InputPeer, 'photo_id' => long];
```
