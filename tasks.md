# Setup

## Create Virtual Environment

In a terminal run the following commands from the root folder of the forked project.

```
python -m venv venv
```

Once that completes, also run this command from the same folder.

Windows

```
venv\Scripts\activate.bat
```

macOS & Linux

```
source venv/bin/activate
```

Now that you are working in the virtualenv, install the project dependencies with the following command.

```
pip install -r requirements.txt
```

## Verify Setup

In order to verify that everything is setup correctly, run the following command, which should show you the failing tests. This is good! We’ll be fixing this test once we jump into the build step.

```
pytest
```

Every time you want to check your work locally you can type that command, and it will report the status of every task in the project.

# Working on tasks
## Task 1: Importing Numpy Library
**`@pytest.mark.test_task1`** In order to start working with the project, load the `numpy` library with an alias `np` at the top of the `tasks/solution.py` file.

## Task 2: Importing the text score file 
**`@pytest.mark.test_task2`** This test to check that the text score file `score.txt` from the `data` directory has been correctly loaded into np dataframe variable using the `np.genfromtxt()` method.

## Task 3: Finding the Max value of the scores
**`@pytest.mark.test_task3`** To find the maximum score use the function .max() from the np library.

## Task 4: Finding the Min value of the scores
**`@pytest.mark.test_task4`** To find the maximum score use the function .min() from the np library.

