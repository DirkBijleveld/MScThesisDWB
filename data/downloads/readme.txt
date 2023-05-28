This folder contains .xlsx files as they are downloaded from the European University Institute website.
 Some changes are made to the files and filenames in order to use them.
This thesis exclusively uses the files for the 8th and 9th European Parliament Sessions.

Download url: https://cadmus.eui.eu/handle/1814/74918
.zip download url (direct): https://cadmus.eui.eu/bitstream/handle/1814/74918/VoteWatch-EP-voting-data_2004-2022.zip?sequence=2&isAllowed=y

Files are renamed to match the following format:
* EP[session number]_RCVs.xlsx - Files containing Roll Call Vote data
* EP[session number]_Voted docs.xlsx - Files containing Vote Data

The following changes apply ONLY to the EP8_Voted docs.xlsx file,
the changes are needed due to mistakes made by the publishers of the .xlsx files.
Without these changes, the software does not function.
1) Rename column 26 (Z) from "Final \nvote?" to "Final vote?"
    -> The "\n" is erroneously included, but makes converting to .csv more difficult.
2) Rename column 20 (T) from "De/Policy area" to "Policy area"

You may now proceed.