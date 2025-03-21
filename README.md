### Run locally with pycharm and debug
1. Set up a remote interpreter 
   1. "On Docker Compose..."
   2. Next
   3. Add python path "/usr/local/bin/python"
2. Set up a Run Configuration called "run"
   1. Select "Django Server"
   2. Set host to "0.0.0.0"
   3. Set port to "8000"

### Run locally with pycharm and debug
Set up a Run Configuration called "run"
1. Select "Django Server"
2. Set host to "0.0.0.0"
3. Set port to "8000"

### Run all pytest with pycharm
1. Go to Run → Edit Configurations
2. Click + and select Python Tests → pytest
3. Script path → set to root of project

### Run specific test with pycharm
Click on arrow next to test, run regular or debug

### Run locally without pycharm or debug
```
docker-compose up --build
```

### Run locally with VScode or Cursor in debug
```
Shift + CMD + D
```