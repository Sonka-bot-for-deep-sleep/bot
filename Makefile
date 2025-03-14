INTERPRETER=python3
DIR_MAIN_PY=./src/main.py
VENV_DIR=bot_venv
ACTIVATE=. $(VENV_DIR)/bin/activate

clone:
	${INTERPRETER} -m venv ${VENV_DIR} && ${ACTIVATE} && pip install -r requirements.txt

run:
	${ACTIVATE} && ${INTERPRETER} ${DIR_MAIN_PY}
