# pageBlockVideo

> Video

[Back to constructors index](/API_docs/constructors/index.html)



Video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|autoplay|[Bool](/API_docs/types/Bool.html) | Optional|Whether the video is set to autoplay|
|loop|[Bool](/API_docs/types/Bool.html) | Optional|Whether the video is set to loop|
|spoiler|[Bool](/API_docs/types/Bool.html) | Optional|
|video\_id|[long](/API_docs/types/long.html) | Yes|Video ID|
|caption|[PageCaption](/API_docs/types/PageCaption.html) | Yes|Caption|



### Type: [PageBlock](/API_docs/types/PageBlock.html)


### Example:

```
$pageBlockVideo = ['_' => 'pageBlockVideo', 'autoplay' => Bool, 'loop' => Bool, 'spoiler' => Bool, 'video_id' => long, 'caption' => PageCaption];
```
