APPLICATION_NAME = {{cookiecutter.project_slug}}

lint:  ##@Code Check code with pylint and flake8
	poetry run python3 -m flake8 $(APPLICATION_NAME)
	poetry run python3 -m pylint $(APPLICATION_NAME)

format:  ##@Code Reformat code with isort
	poetry run python3 -m isort $(APPLICATION_NAME)

run:  ##@Application Run application server
	poetry run python3 -m $(APPLICATION_NAME)

convert:  ##@Code convert .ui files and .qrc files in .py
	cd ./{{cookiecutter.project_slug}}/qt && python auto_generate_files.py "../forms/" -i "resources"

{% if cookiecutter.pyinstaller != 'n' -%}
build:  ##@Code build in Application with Pyinstaller
	pyinstaller {{cookiecutter.project_slug}}.spec
{%- endif %}

clean:  ##@Code Clean directory from garbage files
	rm -fr *.egg-info dist build
