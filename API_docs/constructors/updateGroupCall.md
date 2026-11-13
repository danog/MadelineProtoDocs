# updateGroupCall

> A new groupcall was started

[Back to constructors index](/API_docs/constructors/index.html)



A new groupcall was started

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|live\_story|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[long](/API_docs/types/long.html) | Optional|
|call|[GroupCall](/API_docs/types/GroupCall.html) | Yes|Info about the group call or livestream|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateGroupCall = ['_' => 'updateGroupCall', 'live_story' => Bool, 'peer' => long, 'call' => GroupCall];
```
