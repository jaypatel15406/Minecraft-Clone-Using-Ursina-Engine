# Minecraft Clone build with Ursina Engine :video_game:

Build a clone of the very popular '[Voxel](https://en.wikipedia.org/wiki/Voxel#:~:text=Minecraft%20is%20a%20sandbox%20video,as%20a%20cubic%20%22block%22.&text=The%20voxel%20engine%20allows%20for%20both%20terrain%20destruction%20and%20creation.)' based game called '[Minecraft](https://en.wikipedia.org/wiki/Minecraft)' using '**Ursina Engine**'. The sole purpose of building this clone is to '**Play**' and '**Learn**' together. Because as a kid everyone enjoys playing games. So, this project will help us to understand the mechanism of each functionality in a game. One theory that inclined me to develop this project was a '[Game Theory](https://en.wikipedia.org/wiki/Game_design#:~:text=Game%20theory%20is%20a%20study,discipline%22%20is%20interactive%20decision%20theory.)'. Basically '**Game Theory**' is a study of strategic decision making.

#### What activities can we do in our small 'Minecraft World' :thinking:?

There are multiple activities we can do in this small world. Such as:-
- Creating House
- Build Tree
- Build Towers
- and much more

If you find something interesting to add up to a list. Then feel free to add it.

#### Game Specifications:-

```
01.) Terrain                         :- Desert Terrain
02.) World Dimension                 :- 20 X 20 (400 Voxel Area)
03.) World Time                      :- Day Time
04.) Player View                     :- FPP (First-Person Perspective) View
```

#### Game Settings:- 

```
01.) Player Freefall                 :- Enabled
02.) Player Movement Sound           :- Enabled
03.) Block Placing/ Destroying Sound :- Enabled
04.) FPS (Frame-rate Per Second)     :- Enabled
     Counter
05.) Full Screen Mode                :- Disabled
06.) Hand Movement                   :- Enabled
     while Placing/ Destroying Blocks
```

------------------------------------------------------------------

### How to access game in 'console mode' using 'Python Script'?

Before moving further ahead with a coding part. Make sure you have fullfiled all the '**Requirements**' needed for this project. To verify that open a `Terminal` in the `Root Directory` of the project and write a `Command` given below:-

```
pip install -r requirements.txt
```

Above given `Command` will automatically install all the '**Requirements**' needed for this project. After that you can start exploring '[Main Python Script](https://github.com/jaypatel15406/Minecraft-Clone-Using-Ursina-Engine/blob/main/src/Minecraft_Clone.py)'. To run a game in '**Console Mode**' using this '**Python Script**'. For the same follow the instructions given in the image below:-

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ![Minecraft Clone Python Script Instruction GIF](https://github.com/jaypatel15406/Minecraft-Clone-Using-Ursina-Engine/blob/main/Work%20Demo%20GIFs/Python%20Script.gif)

### How to change 'Game Specifications' And 'Game Settings':-

You can change '**Game Specifications**' And '**Game Settings**' by updating `Code` in '[Minecraft Clone Python File](https://github.com/jaypatel15406/Minecraft-Clone-Using-Ursina-Engine/blob/main/src/Minecraft_Clone.py)'. So, let's see how we can update our app:-

<b>For Update in 'Game Sepcification'</b>

```
# For example if you want to 'Increase' you 'World' Size to '25' Blocks
dimension = 25  # 'Dimension' should be of 25X25 Blocks
for i in range(dimension):
    for j in range(dimension):
        # Initialize 'Voxel' class
        voxel = Voxel(position = (i, 0, j))
```

<b>For Update in 'Game Settings'</b>

```
# For example we have to [lay game in Fullscreen Mode              
window.fullscreen = False
```

> If you are customizing any '**Game Sepcification**' OR '**Game Settings**'. Then it will also impact on your gaming experience and device perfomance as well.

------------------------------------------------------------------

### How to Install Application?

For the Installation process of application. Kindly follow the steps given below:-

**Step 1:-** Go to `/Minecraft-Clone-Using-Ursina-Engine/Application Setup/` Path

**Step 2:-** Click on '**Minecraft_Clone.exe**' Setup file

**Step 3:-** Follow the Steps given in '**Install Wizard**'. 

**Step 4:-** After Installation process gets completed. Click '**Finish**'

**Step 5:-** Congratulations !!! You have successfully Installed Game. Now go to `Path` where you have installed game. And go to that Folder and simply Click '**Sword Icon**' and enjoy game.

If you are still facing problems in the Installation Process then refer the image guide stated below:-

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ![Minecraft Clone Application Installation Instruction GIF](https://github.com/jaypatel15406/Minecraft-Clone-Using-Ursina-Engine/blob/main/Work%20Demo%20GIFs/Application%20Installation.gif)

### If you face error due to '**Windows Defender System**' in accesssing application after the installation process 

This `Error` occured due to `Windows Defender` Settings. It sometime throw error if we install `Software` with `Unknown Auther` or without `LICENSE`. 

### Solution of above mentioned error:-

For the `Solution` of the `issue` mentioned above. Kindly follow the steps given below:-

**Step 1:-** Open '**Windows Security**'

**Step 2:-** Select '**Virus & Protection**' from the left hand side menu

**Step 3:-** Go to '**Virus & threat protection setting**' and select '**Manage Setting**'

**Step 3:-** Turn Off '**Real-time Protection**'

**Step 4:-** Try Accessing Application again

> **NOTE:-** If you are turning ON 'Real-time Protection' then it will locates and stops Malwares from installing or running on your device. You can turn off this setting for a short time before it turn back on automatically.

After the `Installation` Process and `Clearing Security`. If you still facing problem finding `Application`. Kindly follow the image guide given below for the application demo:-

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ![Minecraft Clone Application Demo GIF](https://github.com/jaypatel15406/Minecraft-Clone-Using-Ursina-Engine/blob/main/Work%20Demo%20GIFs/Application%20Demo.gif)

For '**Closing Application**' Press `Alt + Tab` and hover on `X` icon and '**close it**'.

------------------------------------------------------------------

### Game Control Guide:-

|      Keys      |         Actions                   |    
|     :---:      |          :---:                    |
|       w        | To Move Forward                   |
|       a        | To Move Left                      |
|       s        | To Move Backward                  |
|       d        | To Move Right                     |
|    'Space'     | To Jump                           |
|       0        | To Select '**Emerald Ore**' Block |
|       1        | To Select '**Sand**' Block        |
|       2        | To Select '**Stone**' Block       |
|       3        | To Select '**Stone**' Brick       |
|       4        | To Select '**Wood**' Plank        |
|       5        | To Select '**Leaves**'            |
|       6        | To Select '**Obsidian**'          |
|       7        | To Select '**Sponge**'            |
|       8        | To Select '**Gold Ore**' Block    |
|       9        | To Select '**Diamond Ore**' Block |

------------------------------------------------------------------

### For more resources:-

1.) [Ursina Engine Official Documentation](https://www.ursinaengine.org/documentation.html) <br/>
2.) [Ursina Engine Official Cheat Sheet](https://www.ursinaengine.org/cheat_sheet.html) <br/>
3.) [Ursina Engine Official Minecraft Clone Code](https://github.com/pokepetter/ursina/blob/master/samples/minecraft_clone.py)

------------------------------------------------------------------

#### To Contribute to the Project:

1. Choose any open issue from [here](https://github.com/jaypatel15406/Minecraft-Clone-Using-Ursina-Engine/issues). 
2. Comment on the Issue: `Can I work on this?` and Start Exploring it.
3. Make changes to your Fork and Send a PR.

#### To Create a PR (Pull Request):

For Creating Valid PR Successfully. Kindly follow Guide: https://help.github.com/articles/creating-a-pull-request/

#### To Send a PR, Follow Rules Carefully !!   

**Otherwise your PR will be Closed**:

1. For Appropriate PR, follow Title Format: `Fixes #IssueNo : Name of the Issue`

For any Doubts related to the Issues, such as understanding Issue better etc., Comment Down your Queries on the Respective Issue.
