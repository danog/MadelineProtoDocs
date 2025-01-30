---
title: "contacts.contactBirthdays"
description: "Birthday information of our contacts."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/contacts_contactBirthdays.html
---
# Constructor: contacts.contactBirthdays  
[Back to constructors index](/API_docs/constructors/index.html)



Birthday information of our contacts.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|contacts|Array of [ContactBirthday](/API_docs/types/ContactBirthday.html) | Yes|Birthday info|
|users|Array of [User](/API_docs/types/User.html) | Yes|User information|



### Type: [contacts.ContactBirthdays](/API_docs/types/contacts.ContactBirthdays.html)


### Example:

```
$contacts_contactBirthdays = ['_' => 'contacts.contactBirthdays', 'contacts' => [ContactBirthday, ContactBirthday], 'users' => [User, User]];
```  
