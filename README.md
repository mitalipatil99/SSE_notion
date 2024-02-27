# SSE_notion

## Set up

- mouse is controlled by fixed coorinates that map a screen of size ()
- The user
- Keyboard is scalable, when copy-paste function is used insted of press
  - US keyboard
  - or change according to doc
    - Doc suggest '@'
      - https://pyautogui.readthedocs.io/en/latest/keyboard.html
- Assumes a folder named Documents in finder 
- Download paper.pdf and save it on your desktop (make sure this is the only file on the desktop/or the coorinates may be changed)
- If you choose to use your own notion user you have to have the cornell notes template dowloaded (access thourgh: https://www.notion.so/templates/cornell-notes-system)

## User

To test the user, we have created a dummy-user.
Username:sse2024notion@gmail.com
Password:notion2024


## Use case
- [x] Notes
- [x] Bullet points
- [x] Text block
- [x] Insert attachement
- [ ] math equation
- [ ] code block


## Marks

The scritps are written to use both applications in the most efficient way. That means using autocomplete, where that is supporten within the app (ex. @today is tabbet to autocomplete after @t is pressed on keyboard)

Do not use delete (it fucks stuff up), use backspace


## BLOGPOST STUFF 
As students we use various note taking softwares often, but which software is an environmantally conscious choice? In this blogpost we answer this question by comparing the energy consumption between the desktop version and the web version of notion. We present arguments on why one might be a better choice than the other.

At TU Delft many students create, collaborate and organise their notes on Notion. This can be attributed to the fact that Notion allows for creating databases, integration with google drive, github and its use of KaTeX library to render math equations. 

While sustainiabilty might not be the integral aspect of the Notion software we can make it an afterthought and use it in a manner where we reduce overall energy consumption or save your laptops energy.

RQ : Is there a diffrence in energy consumption of Notion on desktop vs browser. 

Methodology :
We conducted two different experiments (login to logout and just making a database/creating an empty page) on two different modes of operation of notion, one mode being desktop and the other mode being notions web application on chrome web browser. We are using the cornell note system template as a use case for both the modes.  We have tried to include all the basic features that users usually use on notion in the workflow pipeline. 
The experiment flow for notion is :
open Desktop app on fullscreen -> login using google sign in option(we created a dummy account  for this experiment) -> create a new page using the cornell system template -> write a page title with some basic text -> make a todo list -> ..............#fill it up#...-> write a math equation -> write a piece of code -> check a todo -> logout 

We ran an automated script to open notion on desktop and the web verion on chrome.
Each of it was run 30 times and to prevent the order of experiments influencing the resulting measurements, the experiments were randomly shuffled.
For each experiment, we took the following measurements:




machine , os and web browser used. 



Experiment :


Results :
graphs 


Replication:


discussion:
practical implications. 


Limitation:
worth noting the response time on web vs desktop , 
accesibililty to online vs offline features 



Conclusion 









