<br />
<p align="center">
  <a href="https://github.com/winnllam/socialmedia-image-scapel">
    <img src="images/logo.png" alt="Logo">
  </a>

  <h3 align="center">Image duplication made easy.</h3>

  <p align="center">
    REST API · <a href="https://socialmedia-image-scapel.vercel.app/swagger">Swagger</a>
  </p>
</p>

<details open="open">
  <summary>Table of Contents</summary>
  <ul>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#running-the-app">Running the App</a></li>
    <li><a href="#deployment">Deployment</a></li>
    <li><a href="#sources">Sources</a></li>

  </ul>
</details>

## About The Project

Tired of uploading pictures to your social media, but also need them on your personal websites? This is an API that extracts thumbnail URLs of shots made by a user on different media platforms. This enables the user to display their creative pieces in different locations while only posting on one.

### Built With

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Vercel](https://vercel.com/)

## Usage

Currently accessible at: https://socialmedia-image-scapel.vercel.app/

Use it to display imagines on your [website](https://winnllam.github.io/media). This keeps you from re-uploading imagines into different locations - just post them in your social media and get the image links.

## Getting Started

To get a local copy up and running, follow the below steps.

### Prerequisites

You will need Python to be able to run the code.

### Installation

Clone the repo:

```sh
git clone https://github.com/winnllam/socialmedia-image-scapel.git
```

Clone the repository and create your virtual environment:
```
python -m venv venv/
```

## Running the App

Activate the virtual environment:
```
source venv/scripts/activate
```

Run the code on [localhost](http://127.0.0.1:5000/) (port 5000):
```
cd venv
flask run
```

Deactivate the virtual environment:
```
deactivate
```

## Deployment

Use `vercel` in the terminal to set up the initial deployment. You will need to install vercel:

```
npm i -g vercel
```

For each deployment after, use:
```
vercel --prod
```

## Sources
* https://stackabuse.com/deploying-a-flask-application-to-heroku/
* https://andrewbaisden.medium.com/how-to-deploy-a-python-flask-app-to-vercel-ff4a63d312f4
* https://github.com/winnllam/dribbble-tn-scapel (now deprecated)