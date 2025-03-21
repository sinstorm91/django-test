### Run locally with pycharm and debug
1. Set up a remote interpreter 
   1. "On Docker Compose..."
   2. Next
   3. Add python path "/usr/local/bin/python"
2. Set up a Run Configuration called "debug"
   1. Select "Django Server"
   2. Set host to "0.0.0.0"
   3. Set port to "8000"

### Run locally with pycharm and no debug
Set up a Run Configuration called "run"
1. Select "Django Server"
2. Set host to "0.0.0.0"
3. Set port to "8000"
4. Add env variable DJANGO_DEBUG=False

### Run all pytest with pycharm
1. Go to Run → Edit Configurations
2. Click + and select Python Tests → pytest
3. Script path → set to root of project

### Run specific test with pycharm
Click on arrow next to test, run regular or debug

### Profile tests
Run the app
```
DJANGO_DEBUG=False docker-compose up --build
```
Exec into the container
```
docker exec -it django_debug bash
```
Inside the container run the profiler and save the results to /app/profiler_data/pytest_profile.pstats 
```
python -m cProfile -o /app/profiler_data/pytest_profile.pstats -m pytest
```
Visualize the profile with you preferred tool from your local machine
```
snakeviz ./profiler_data/pytest_profile.pstats
```

### Run locally without pycharm or debug
```
DJANGO_DEBUG=False docker-compose up --build
```

