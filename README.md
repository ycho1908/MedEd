<img src="./frontend/src/MedEd_logo.png" alt="MedEd Logo" width="200" height="200"><br/>

_MedEd_ is a full stack web application that answers any medical questions or concerns that the user/patient has.

## Features

- **AI Chatbot**: From our homepage, users will be able to ask questions to the AI medical assistant and receive answers (also based on your previous prompts as well).

## Technologies
- React.js
- FastAPI
- Gradio

## Setup
In order to run a local instance of MedEd, follow the instructions below.

<details><summary><b>Show instructions (If cloning from GitHub repository)</b></summary>

1. Create a new directory and startup a virtual environment

```shell
mkdir webapp
cd webapp
python3 -m venv gradio-env
source gradio-venv/bin/activate
```

2. Clone this repository and change into its directory

```shell
git clone https://github.com/ycho1908/MedEd.git
```

3. Install dependencies

```shell
pip install -r MedEd/requirements.txt
pip install --upgrade pip

pip install gradio_client fastapi uvicorn   // for backend
```

4. If you would want the '.env' file, please reach out to us. Download `.env` file after you have received them into the `webapp/MedEd` directory
  
5. Run the backend server
```shell
uvicorn main:app --reload
```

7. In a separate terminal, run the webapp!
```shell
cd webapp
cd MedEd/frontend
npm -f install
npm start
```

9. Go to http://127.0.0.1:3000/ in a browser to view the project

</details>

## Authors
_MedEd_ was made as a project by Yehyeon (Evelyn) Cho [Computer Science at UCLA] and Rebecca Su [Computer Science at UCI]. 


**Made by**: [Yehyeon (Evelyn) Cho](mailto:yehyeoncho@gmail.com), [Rebecca Su](rcsu@uci.edu)

