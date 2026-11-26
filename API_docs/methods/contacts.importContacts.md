# contacts.importContacts

> Imports contacts: saves a full list on the server, adds already registered contacts to the contact list, returns added contacts and their info.

[Back to methods index](index.html)



Imports contacts: saves a full list on the server, adds already registered contacts to the contact list, returns added contacts and their info.

Use [contacts.addContact](../methods/contacts.addContact.html) to add Telegram contacts without actually using their phone number.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|contacts|Array of [InputContact](/API_docs/types/InputContact.html) | List of contacts to import | Yes|


### Return type: [contacts.ImportedContacts](/API_docs/types/contacts.ImportedContacts.html)

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

$contacts_ImportedContacts = $MadelineProto->contacts->importContacts(contacts: [$InputContact, $InputContact], );
```
