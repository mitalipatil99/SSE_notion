# SSE Notion

## Introduction

This repository contains scripts and instructions for conducting energy consumption experiments comparing the desktop and web versions of Notion.

## Setup Instructions

### System Requirements

- **Operating System:** macOS Sanoma 14.2.1 (23C71)
- **Hardware:** MacBook Air 2020 with 8GB RAM
- **Display:** 13.3-inch (2560 × 1600)
- **Google Chrome Version:** 122.0.6261.69
- **Notion App Version:** 3.2.1

### Additional Setup

- **Keyboard:** US/ABC
- **Resources:** Ensure the PDF found in `resources/SSE.pdf` is locally saved on the desktop as the only file. This PDF is uploaded to Notion as part of the experiment run.
  - **Finder View:** Set Finder to "icon only" view and ensure the icon is placed at the default location or move it to the top left corner.
- **Mouse Control:** The mouse is controlled by fixed coordinates using `pyauto.moveT(x, y)`. If your computer's screen size or software versions differ, adjust the coordinates in `application_script.py`, `chromewebscript.py`, and `main.py`.
- **energiBridge.py**: Line #19 and #22 in `energiBridge.py` need to be changed to the correct path (see EnergiBridge section below)

### Notion User Credentials

- **Username:** sse2024notion@gmail.com
- **Password:** notion2024

### EnergiBridge Setup

1. Download the EnergiBridge repository from [here](https://github.com/tdurieux/energibridge).
2. Navigate to the folder containing the EnergiBridge executable file (`energibridge-v0.0.4-aarch64-apple-darwin`). Note the path to this file for configuration.

## Tested Use Cases

Below follows a description on how you can expect the script to act, following estimated timestap (from desktop) for each function (t=0 when terminal executed line #19/22 is executed)

### Login
- **Open Chrome** *(3s)* - This is done to ensure chrome is in fullscreen (and cooridnates in script correct) when redirected from the desktop-app under login.
  - **Log in on chrome user** *(8s-11s)* - Assumes two profiles on chrome, i.e. you need to select one (and the second is selected)
- **Open notion** *(12s)*
  - Redirecting to chrome (15s-21s)
    - Login to notion from chrome (19s)
  - Redirectin to notion (22s)
- **Close chrome** *(26s)*
 
### New page 
- **Create new page** *(30s)*
- **Get Cornell template** *(48s)* 

### Write page
- **Delete description** *(56s-60s)*
- **Heading** *(61s-70s)*
- **Date** *(63s-77s)*
- **Topic** *(80s-81s)*
- **Bullet point** *(83s-93)*
- **To Do list** *(93s-90)**

### Material
- **Finding file to upload** *(112s-118s)*
  - Starting upload (119s)
- **New linked page** *(125s-169s)*

### Math
- **Write math equation** *(175s-185s)*
  
### Code
- **Notes** *(191s)*
- **Write code** *(196s-208s)*
- **Check checkbox** *(209s)*

### Log out
- **Click on user** *(214s)*
- **Click log out and log out** *(216s-220s)
