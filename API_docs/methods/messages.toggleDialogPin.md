# messages.toggleDialogPin

> Pin/unpin a dialog

[Back to methods index](index.html)



Pin/unpin a dialog

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|pinned|[Bool](/API_docs/types/Bool.html) | Whether to pin or unpin the dialog | Optional|
|peer|[InputDialogPeer](/API_docs/types/InputDialogPeer.html) | The dialog to pin | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->toggleDialogPin(pinned: $Bool, peer: $InputDialogPeer, );
```
