# Klaus

A secret santa discord chat bot. This bot will allow administrators to run a secret santa with the bot doing all the heavy lifting.

## Dev Goals

* Allow participants to signup
* Keep track of participants information
  * Name
  * Contact/Shipping information
  * Custom attributes you collect from participants
* Participants interaction
  * Chat with the bot to get your secrets info
  * On demand FAQ - general event support
  * Opt-in switch to reveal your identity
* Shipping Management
  * Notify Admins of Shipped status
  * Participants can enter shipping info to be notified of status
* Admin
  * Homepage
    * Number of participants
    * Amount of gifts shipped
    * Important Event dates
    * Activity Panel
  * Participants page
    * Address hidden by default
      * Optional opt-in to reveal to admin
    * Export participants
    * Shipped Status
    * Dropdown with participant info

## Infrastructure Goals

CI/CD Pipeline

* Automated Package Building Process
* Automated Package Release
* Automated Package Versioning

## Stack

* Python
* Github Actions
* Linode Instance

[Public Dev Diary](https://forum.level1techs.com/t/devember2020-klaus-secret-santa-discord-bot/163657)
