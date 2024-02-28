# SSE_notion

## Set up, we can add it to replication code github readme

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
- Google chrome V. 122.0.6261.69
- Notion app v. 3.2.1
- Laptop
  - MacBook air 2020
  - Memory 8GB
  - macOS Sanoma 14.2.1 (23C71)
  - Display: 13,3-inch (2560 × 1600)


## User

To test the user, we have created a dummy-user.
Username:sse2024notion@gmail.com
Password:notion2024

## Use case

- [x] Notes
- [x] Bullet points
- [x] Text block
- [x] Insert attachement
- [x] math equation
- [x] code block

## EnergiBridge

- Download the repository from: https://github.com/tdurieux/energibridge
- CD into the folder that holds the energibridge exec file (energibridge-v0.0.4-aarch64-apple-darwin )
- 

## Marks

The scritps are written to use both applications in the most efficient way. That means using autocomplete, where that is supporten within the app (ex. @today is tabbet to autocomplete after @t is pressed on keyboard)

Do not use delete (it fucks stuff up), use backspace

## BLOGPOST STUFF

As students we use various note taking softwares often, but which software is an environmantally conscious choice? In this blogpost we answer this question by comparing the energy consumption between the desktop version and the web version of notion. We present arguments on why one might be a better choice than the other.

At TU Delft many students create, collaborate and organise their notes on Notion. This can be attributed to the fact that Notion allows for creating databases, integration with google drive, github and its use of KaTeX library to render math equations.

While sustainiabilty might not be the integral aspect of the Notion software we can make it an afterthought and use it in a manner where we reduce overall energy consumption or save your laptops energy.

RQ : Is there a diffrence in energy consumption of Notion on desktop vs browser.

Methodology :
We conducted two different experiments (login to logout and just making a database/creating an empty page) on two different modes of operation of notion, one mode being desktop and the other mode being notions web application on chrome web browser. We are using the cornell note system template as a use case for both the modes. We have tried to include all the basic features that users usually use on notion in the workflow pipeline.
The experiment flow for notion is :
open Desktop app on fullscreen -> login using google sign in option(we created a dummy account for this experiment) -> create a new page using the cornell system template -> write a page title with some basic text -> make a todo list -> ..............#fill it up#...-> write a math equation -> write a piece of code -> check a todo -> logout

We ran an automated script to open notion on desktop and the web version on chrome.
Each of it was run 30 times and to prevent the order of experiments influencing the resulting measurements, the experiments were randomly shuffled.
For each experiment, we took the following measurements:.............

In addition to the experiment measurements, we also provide a baseline measurement to give an idea of how background processes impact the measurements. The baseline measurement is a 60 second measurement with the same settings as in the experimental setup but with no programs open except background processes.

Experimental set up :

We conducted the experiments on MacBook Air M1 Laptop with 8GB RAM running macOS Sanoma 14.2.1 (23C71). The specific software used for the experiment is:
| Software      | Vesrion |
|---------------|---------|
| Notion Desktop| 3.2.1     |
| Google Chrome Browser| 122.0.6261.69     |

The energy consumption was measured using [EnergiBridge](https://github.com/tdurieux/EnergiBridge)

Before executing the experiments it is important to record the state of the system under test so that the state can be kept as consistent as possible between experiments. In addition to the hardware and software specifications above, we made sure that the laptop was in the following state to minimize confounding factors:

1: Stable Wifi6 Connection with average throughput of 250mbps.
2: Notifications turned off 
3: Power cable plugged in 
3: Screen brightness set to 100 %
4: No applications/programs/services running in the background. 

Since hardware temperature affects the energy consumption among the experiment runs which impacts the results, we set up a warm up routine with a dummy task of calculating fibonnaci sequence for 30 seconds to minimise the temperature difference. 
The experiment structure was as follows :
1: warm up CPU
2: Shuffle and run 60 iterations(30 for desktop experiment and 30 for chrome broswer experiment each)
   2.1: Start measuring 
   2.2: Start Notion Workflow (mentioned above) using an automated script 
   2.3: Stop Measuring
   2.4: Wait for 30 seconds

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
