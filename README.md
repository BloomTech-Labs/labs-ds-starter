# Labs DS starter

- [Big picture](#big-picture)
- [Tech stack](#tech-stack)
- [Getting started](#getting-started)
- [File structure](#file-structure)
- [Deploy to AWS](#deploy-to-aws)
- [Example: Data visualization](#example-data-visualization)
- [Example: Machine learning](#example-machine-learning)

## Big picture

This template has starter code to deploy an API for your machine learning model and data visualizations.

You can see the [template deployed on AWS](https://ds.labsscaffolding.dev/) as-is.

This diagram shows two different ways to use Python web frameworks. Both ways are good! The first way is what you learned in DS Unit 3, with Flask. The second way is more common in Build Weeks & Labs. 

![](https://user-images.githubusercontent.com/7278219/87967396-5a6fed80-ca84-11ea-902a-890cfa6115d3.png)

Instead of Flask, we'll use FastAPI. It's similar, but faster, with automatic interactive docs. For more comparison, see [FastAPI for Flask Users](https://amitness.com/2020/06/fastapi-vs-flask/).

You'll build and deploy a Data Science API. You'll work cross-functionally with your Web teammates to connect your API to a full-stack web app!

![](https://user-images.githubusercontent.com/7278219/87967579-a4f16a00-ca84-11ea-9f90-886b3cf1a25c.png)

## Tech stack
- [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html): Platform as a service, hosts your API.
- [Docker](https://www.docker.com/blog/tag/python-env-series/): Containers, for reproducible environments.
- [FastAPI](https://fastapi.tiangolo.com/): Web framework. Like Flask, but faster, with automatic interactive docs.
- [Flake8](https://flake8.pycqa.org/en/latest/): Linter, enforces PEP8 style guide.
- [Plotly](https://plotly.com/python/): Visualization library, for Python & JavaScript.
- [Pytest](https://docs.pytest.org/en/stable/): Testing framework, runs your unit tests.

## Getting started

[Create a new repository from this template.](https://github.com/Lambda-School-Labs/labs-ds-starter/generate)

Clone the repo
```
git clone https://github.com/YOUR-GITHUB-USERNAME/YOUR-REPO-NAME.git

cd YOUR-REPO-NAME
```

Build the Docker image
```
docker-compose build
```

Run the Docker image
```
docker-compose up
```

Go to `localhost:8000` in your browser.

![image](https://user-images.githubusercontent.com/7278219/89348227-cef48000-d671-11ea-90b1-d02cd9af8fbc.png)

You'll see your API documentation:

- Your app's title
- Your description
- An endpoint for POST requests, `/predict`
- An endpoint for GET requests, `/viz`

Click the `/predict` endpoint's green button.

![image](https://user-images.githubusercontent.com/7278219/89348390-1bd85680-d672-11ea-90f8-26b9e65cbe86.png)

You'll see the endpoint's documentation, including:

- Your function's docstring, """Make random baseline predictions for classification problem."""
- Request body example, as [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON) (like a Python dictionary)
- A button, "Try it out"

Click the "Try it out" button.

![image](https://user-images.githubusercontent.com/7278219/87966677-39f36380-ca83-11ea-97f4-313bc11d3f19.png)

The request body becomes editable. 

Click the "Execute" button. Then scroll down.

![image](https://user-images.githubusercontent.com/7278219/87966896-948cbf80-ca83-11ea-9740-d0801148b1f3.png)

You'll see the server response, including:

- [Code 200](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200), which means the request was successful.
- The response body, as [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON), with random baseline predictions for a classification problem.

***Your job is to replace these random predictions with real predictions from your model.*** Use this starter code and documentation to deploy your model as an API!

## File structure

```
project
├── requirements.txt
└── app
    ├── __init__.py
    ├── main.py
    ├── api
    │   ├── __init__.py
    │   ├── predict.py
    │   └── viz.py    
    └── tests
        ├── __init__.py
        ├── test_main.py
        ├── test_predict.py
        └── test_viz.py
```

`requirements.txt` is where you add Python packages that your app requires. Then run `docker-compose build` to re-build your Docker image.

`app/main.py` is where you edit your app's title and description, which are displayed at the top of the your automatically generated documentation. This file also configures "Cross-Origin Resource Sharing", which you shouldn't need to edit. 

- [FastAPI docs - First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [FastAPI docs - Metadata](https://fastapi.tiangolo.com/tutorial/metadata/)
- [FastAPI docs - CORS](https://fastapi.tiangolo.com/tutorial/cors/)

`app/api/predict.py` defines the **Machine Learning** endpoint. `/predict` accepts POST requests and responds with random predictions. In a notebook, train your model and pickle it. Then in this source code file, unpickle your model and edit the `predict` function to return real predictions.

- [Scikit-learn docs - Model persistence](https://scikit-learn.org/stable/modules/model_persistence.html)
- [Keras docs - Serialization and saving](https://keras.io/guides/serialization_and_saving/)

When your API receives a POST request, FastAPI automatically parses and validates the request body JSON, using the `Item` class attributes and functions. Edit this class so it's consistent with the column names and types from your training dataframe. 

- [FastAPI docs - Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [FastAPI docs - Field additional arguments](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#field-additional-arguments)
- [calmcode.io video - FastAPI - Json](https://calmcode.io/fastapi/json.html)
- [calmcode.io video - FastAPI - Type Validation](https://calmcode.io/fastapi/type-validation.html)
- [pydantic docs - Validators](https://pydantic-docs.helpmanual.io/usage/validators/)

`app/api/viz.py` defines the **Visualization** endpoint. Create your own Plotly visualizations in notebooks. Then add your code to this source code file. Your web teammates can use [react-plotly.js](https://github.com/Lambda-School-Labs/labs-spa-starter/tree/main/src/components/pages/ExampleDataViz) to show the visualizations.

![react-plotly.js animation](https://media.giphy.com/media/j3QG8qVBQcpKvCfO3T/giphy.gif)

- [Lambda School docs - Data visualization with React & Plotly](https://github.com/Lambda-School-Labs/labs-spa-starter/tree/main/src/components/pages/ExampleDataViz). This is the code for the example above. Your web teammates can reuse this as-is.
- [Plotly docs](https://plotly.com/python/)


`app/tests/test_*.py` is where you edit your pytest unit tests. 

- [FastAPI docs - Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [calmcode.io videos - FastAPI - Testing](https://calmcode.io/fastapi/testing-one.html)
- [calmcode.io videos - pytest](https://calmcode.io/pytest/introduction.html)

## Deploy to AWS

[Get your AWS access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey).

Install [AWS Command Line Interface](https://aws.amazon.com/cli/).

[Configure AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config):
```
aws configure
```

Install AWS Elastic Beanstalk CLI:
```
pip install pipx
pipx install awsebcli
```

Follow [AWS EB docs](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/single-container-docker.html#single-container-docker.test-remote):

Use Docker to build the image locally, test it locally, then push it to Docker Hub.

```
docker build -f project/Dockerfile -t YOUR-DOCKER-HUB-ID/YOUR-IMAGE-NAME ./project

docker login

docker push YOUR-DOCKER-HUB-ID/YOUR-IMAGE-NAME
```

Edit the image name in the  `Dockerrun.aws.json` file. Replace the placeholder `YOUR-DOCKER-HUB-ID/YOUR-IMAGE-NAME` with your real values. 

Then use the EB CLI:
```
git add --all

git commit -m "Your commit message"

eb init -p docker YOUR-APP-NAME --region us-east-1

eb create YOUR-APP-NAME

eb open
```

To redeploy:

- `git commit ...`
- `docker build ...`
- `docker push ...`
- `eb deploy`
- `eb open`

## Example: Data visualization

Labs projects will use [Plotly](https://plotly.com/python/), a popular visualization library for both Python & JavaScript.

Follow the [getting started](#getting-started) instructions.

Edit `app/main.py` to add your API `title` and `description`.

```python
app = FastAPI(
    title='World Metrics DS API',
    description='Visualize world metrics from Gapminder data',
    version='0.1',
    docs_url='/',
)
```

Prototype your visualization in a notebook.

```python
import plotly.express as px

dataframe = px.data.gapminder().rename(columns={
    'year': 'Year', 
    'lifeExp': 'Life Expectancy', 
    'pop': 'Population', 
    'gdpPercap': 'GDP Per Capita'
})

country = 'United States'
metric = 'Population'
subset = dataframe[dataframe.country == country]
fig = px.line(subset, x='Year', y=metric, title=f'{metric} in {country}')
fig.show()
```

Define a function for your visualization. End with `return fig.to_json()`

Then edit `app/api/viz.py` to add your code.

```python
import plotly.express as px

dataframe = px.data.gapminder().rename(columns={
    'year': 'Year', 
    'lifeExp': 'Life Expectancy', 
    'pop': 'Population', 
    'gdpPercap': 'GDP Per Capita'
})

@app.get('/worldviz')
async def worldviz(metric, country):
    """
    Visualize world metrics from Gapminder data

    ### Query Parameters
    - `metric`: 'Life Expectancy', 'Population', or 'GDP Per Capita'
    - `country`: [country name](https://www.gapminder.org/data/geo/), case sensitive

    ### Response
    JSON string to render with react-plotly.js
    """
    subset = dataframe[dataframe.country == country]
    fig = px.line(subset, x='Year', y=metric, title=f'{metric} in {country}')
    return fig.to_json()
```

Test locally, then [deploy to AWS](#deploy-to-aws). 

Your web teammates will re-use the [data viz code & docs in our `labs-spa-starter` repo](https://github.com/Lambda-School-Labs/labs-spa-starter/tree/main/src/components/pages/ExampleDataViz). The web app will call the DS API to get the data, then use `react-plotly.js` to render the visualization. 

#### Plotly Python docs
- [Example gallery](https://plotly.com/python/)
- [Setting Graph Size](https://plotly.com/python/setting-graph-size/)
- [Styling Plotly Express Figures](https://plotly.com/python/styling-plotly-express/)
- [Text and font styling](https://plotly.com/python/v3/font/)
- [Theming and templates](https://plotly.com/python/templates/)

#### Plotly JavaScript docs
- [Lambda `labs-spa-starter` data viz code & docs](https://github.com/Lambda-School-Labs/labs-spa-starter/tree/main/src/components/pages/ExampleDataViz)
- [Example gallery](https://plotly.com/javascript/)
- [Fundamentals](https://plotly.com/javascript/plotly-fundamentals/)
- [react-plotly.js](https://plotly.com/javascript/react/)


## Example: Machine learning

Follow the [getting started](#getting-started) instructions.

Edit `app/main.py` to add your API `title` and `description`.

```python
app = FastAPI(
    title='House Price DS API',
    description='Predict house prices in California',
    version='0.1',
    docs_url='/',
)
```

Edit `app/api/predict.py` to add a docstring for your predict function and return a naive baseline. 

```python
@router.post('/predict')
async def predict(item: Item):
    """Predict house prices in California."""
    y_pred = 200000
    return {'predicted_price': y_pred}
```

In a notebook, explore your data. Make an educated guess of what features you'll use.

```python
import pandas as pd
from sklearn.datasets import fetch_california_housing

# Load data
california = fetch_california_housing()
print(california.DESCR)
X = pd.DataFrame(california.data, columns=california.feature_names)
y = california.target

# Rename columns
X.columns = X.columns.str.lower()
X = X.rename(columns={'avebedrms': 'bedrooms', 'averooms': 'total_rooms'})

# Explore descriptive stats
X.describe()
```

```python
# Use these 3 features
features = ['bedrooms', 'total_rooms', 'house_age']
```

Edit the class in `app/api/predict.py` to use your features.

```python
class House(BaseModel):
    """Use this data model to parse the request body JSON."""
    bedrooms: int
    total_rooms: float
    house_age: float

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

@router.post('/predict')
async def predict(house: House):
    """Predict house prices in California."""
    X_new = house.to_df()
    y_pred = 200000
    return {'predicted_price': y_pred}
```

Test locally, then [deploy to AWS](#deploy-to-aws) with your work-in-progress. Now your web teammates can make POST requests to your API endpoint.

In a notebook, train your pipeline and pickle it. See these docs:

- [Scikit-learn docs - Model persistence](https://scikit-learn.org/stable/modules/model_persistence.html)
- [Keras docs - Serialization and saving](https://keras.io/guides/serialization_and_saving/)

Get version numbers for every package you used in your pipeline. Add these packages to your `requirements.txt` file with their exact version numbers. Then run `docker-compose build` to re-build your Docker image.

Edit `app/api/predict.py` to unpickle your model and use it in your predict function. 

Now you are ready to re-deploy! 🚀