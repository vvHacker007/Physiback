# NTL Hack 2022
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)<br>
Repository to hold code for the '*exercise posture analysis*' project that is being presented in an internal hackathon at NextTech Lab Hack 2022.
<br>

## Problem Inspiration<br>
<img src="assets/cctv_system.jpg" width = "500px"><br>
A plethora of surveillance devices are being used by the Defense Services for supervision and monitoring. However, most of them are manually operated at the cost of enormous amounts of time and manual labour.<br>
<br>

## Problem Description<br>
Present state-of-the-art Surveillance Devices require both consistent manual assistance and time for their successful operation. This results in a considerable loss of manual and technical resources.
<br>

## Proposed Solution<br>
We propose a Deep Learning Application that will be able to solve the above mentioned problems. 
- Our application named ‘Cap-Bot’ is capable of running Image Captioning on multiple CCTV footages and storing the captions along with the camera number and the time of capture in a convenient log.<Br>
<img src = "assets/cameraui.jpg" width = "500px"><br>
- The file of saved captions can then be used to look up for incidents from any instant of time just by entering a few keywords.  The returned camera number and time slot can then be used to obtain the required CCTV footage.<br>
<img src = "assets/search_tab.png" width = "500px"><br>
  
### Check out the [Project Proposal](https://www.youtube.com/watch?v=Sr8dNQMBRZI) for our product.

## Advantages and Features
- Interface to map CCTV Location in a defined area and eventually help single out points of interest.<br>
<img src = "assets/locations.png" width = "500px"><br>
- Since our model relies on Deep Learning, the time can be reduced considerably as we are resorting to an automatic searching operation.<br>
<img src = "assets/dl.png" width = "500px"><br>
- Since the information is purely textual, the encryption of information is way easier than pictorial.<br>
<img src = "assets/encrypt.png" width = "500px"><br>
  
## Steps of Deployment
- [x] Training the Model
- [x] Write the Search Module
- [x] Captioning UI
- [x] Search UI
- [x] Perfecting Search feature 
- [x] Resolving Backend
- [x] Encryption of Generation Captions<br>
<i>Extra Feature</i>
- [ ] CCTV Localization with results


## Using the deployed version of the web application
Please download the <a href = "https://drive.google.com/drive/folders/10RaV7DTsFVgdYeJZIyveyeJKhfvFiKT2?usp=sharing">Model Checkpoints</a> and move the file to the <a href = "https://github.com/aryankargwal/capbot2.0/tree/main/camera">camera</a> folder.

- Setting up the Python Environment with dependencies 

        pip install -r requirements.txt
- Cloning the Repository: 

        git clone https://github.com/aryankargwal/capbot2.0
- Entering the directory for captioning: 

        cd capbot2.0/camera
- Running the captioning web application:

        streamlit run feed.py
- Entering the directory for searching: 

        cd capbot2.0/search
- Running the searching web application:

        streamlit run search.py
- Stopping the web application from the terminal

        Ctrl+C
        
<hr>

## License
This project is under the Apache License. See [LICENSE](LICENSE) for Details.

## Contributors

<table>
<tr align="center">
<td>

Abhijeet Jha

<p align="center">
<img src = "https://avatars.githubusercontent.com/u/67542982?v=4"  height="120" alt="Aryan Kargwal">
</p>
<p align="center">
<a href = "https://github.com/abhijeetjha602"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/abhijeetjha602/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>

<td>

Aditya Mukherjee

<p align="center">
<img src = "https://avatars.githubusercontent.com/u/67542982?v=4"  height="120" alt="Indira Dutta">
</p>
<p align="center">
<a href = "https://github.com/adityamukherjee42"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/aditya-mukherjee-817a17190/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>

<td>

Kunal Mundada

<p align="center">
<img src = "https://avatars.githubusercontent.com/u/53429438?v=4"  height="120" alt="Rusali Saha">
</p>
<p align="center">
<a href = "https://github.com/AlKun25"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/kunalmundada/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>

<td>

Vedansh Vijaywargiya

<p align="center">
<img src = "https://avatars.githubusercontent.com/u/60468275?v=4"  height="120" alt="person">
</p>
<p align="center">
<a href = "https://github.com/vvHacker007"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/vedansh-vijaywargiya/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>
  </table>
</tr>
  </table>


<p align="center">
crafted with <span style="color: #8b0000;">&hearts;</span> by team <b>Missing-Colon</b>
</p>
