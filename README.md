# NTL Hack 2022
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)<br>
Repository to hold code for the '*exercise posture analysis*' project that is being presented in an internal hackathon at NextTech Lab Hack 2022.
<br>

## Problem Inspiration<br>
<br>
<img align='center'  src="Images/3.png"><br>
<br>
The interest in Fitness and Gym is on the rise, and people have started knowing the importance of fitness and health in these trying times. With Gym costly for many  and lack of proper guidance. Injuries have become very frequent. .<br>
<br>




## Problem Description<br>
*What are the problems we face if we don't exercise for a long time?*
<br>
<br>
<img src="Images/problems.png"><br>
<br>
*What are the benifits we get if we exercise regularly?*
<br>
<br>
<img src="Images/2.png"><br>
<br>
There are multiple issues that people face in relation with the exercises, fitness and gym scenario, few of them are given as follows:
- The gym costs a lot of money, time. Many people don't want to pay for a gym membership if they're not going that often.
- Proper feedback and guidance is a must in exercise or else it can lead to painful and sometimes crippling injuries  
- Due to covid, many have opted to do workouts at home. But with , with more than 1000 youtube videos, people find it hard to actually understand the correct technique
<br>

## Proposed Solution<br>
Keeping all of this in mind, we came up with a live workout analysis called Physisback. You can now analyze your past workouts or even your current workout and get feedback all from your home. Physiback uses the power of AI and helps users to get a grade on their exercise and also suggestions all from the comfort of their home<br><br>
<!-- ![DEMO]("https://github.com/vvHacker007/NTL_Hack_2022/blob/main/Assets/Videos/DEMO.mp4") -->

### Check out the [Project Proposal](https://www.canva.com/design/DAE6Ft86pmE/6XbJ9HAkYR17zx3zRZ6uOg/edit) for our product.

## Features:
- **Auto Feedback**:  You can get Feedback on your exercises about your posture and the corrections required to improve it.<br>
- **Auto Grading**: Using our calculation, we grade each repetition your perform in your video.<br>
- **Post-workout analysis**: You can upload your CSV of past workout and analyze it.<br>
  
## Progress points:
- [x] Develop a basic Streamlit website
- [x] Video input through live feed or recorded video
- [x] Image processing
- [x] Pose estimation
- [x] Repetition analysis 
- [x] Download analysis through CSV<br>
<i>Extra Feature</i>
- [ ] Multiple angle analysis


## Using the deployed version of the web application
<!-- Please download the <a href = "https://drive.google.com/drive/folders/10RaV7DTsFVgdYeJZIyveyeJKhfvFiKT2?usp=sharing">Model Checkpoints</a> and move the file to the <a href = "https://github.com/aryankargwal/capbot2.0/tree/main/camera">camera</a> folder. -->

- Setting up the Python Environment with dependencies 

        pip install -r requirements.txt
- Cloning the Repository: 

        git clone https://github.com/vvHacker007/NTL_Hack_2022
- Entering the directory for captioning: 

        cd NTL_Hack_2022
- Running the captioning web application:

        streamlit run physio.py
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
<img src = "https://avatars.githubusercontent.com/u/60893631?v=4"  height="120" alt="Indira Dutta">
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
crafted with <span style="color: #8b0000;">&hearts;</span> by team <b>Hum bhi bana lenge</b>
</p>
