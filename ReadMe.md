# <center> Data Version Control <center>

### Demo

##### Initiate Git Repository

1) Create a folder for starting project
> mkdir demo1   
> cd demo1

2) Let's create git repository before we start tracking the data
> git init

3) Initiating the DVC repo
> dvc init

4) Pushing data to cloud
> dvc remote add -d storage gdrive://   
> dvc remote add -d -f storage gdrive://1WDMvcQMogjojcVfw1gkrC_JsWV3KgWRf

5) Commit to git
> git commit .dvc/config -m "Configuring remote storage"

6) Copy the data files to git/dvc repo
7) Add data to dvc
> dvc add data      

8) Adding .gitignore and *.dvc files to git to track the changes
> git add data.dvc .gitignore   
> git commit -m "Version 1 Data"

9) View the contents of  *.dvc file
> cat data.dvc

10) Pushing data to remote storage
> dvc push

11) Add new Data
> dvc add data

12) Track data changes in git
> git add data.dvc

13) Commit Changes to 
> git commit -m "Version 2 Data"

14) Push the data to cloud
> dvc push

15) Checkout data to previous commit
> git checkout HEAD^1 data.dvc

16) Copy python scripts
> git add .     
> git commit -m "Data Cleaning and Training Scripts"        
> git log --oneline

17) Running Logistic Regression
> python -m training

18) Adding model to dvc
> dvc add model

19) updating model and git ignore files
> git add .gitignore model.dvc

20) Modify model to RandomForest
> Change config file

21) Training the model again
> python -m training

22) Add new model to DVC
> dvc add model         
> git add .     
> git commit -m "Random Forest V1 Data"