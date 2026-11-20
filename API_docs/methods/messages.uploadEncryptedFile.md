# messages.uploadEncryptedFile

> Upload encrypted file and associate it to a secret chat (without actually sending it to the chat).

[Back to methods index](index.html)



Upload encrypted file and associate it to a secret chat (without actually sending it to the chat).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Secret chat ID, Update, EncryptedMessage or InputEncryptedChat](/API_docs/types/InputEncryptedChat.html) | The secret chat to associate the file to | Yes|
|file|[File path or InputEncryptedFile](/API_docs/types/InputEncryptedFile.html) | The file | Optional|


### Return type: [EncryptedFile](/API_docs/types/EncryptedFile.html)

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

$EncryptedFile = $MadelineProto->messages->uploadEncryptedFile(peer: $InputEncryptedChat, file: $InputEncryptedFile, );
```
