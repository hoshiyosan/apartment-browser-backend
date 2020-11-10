include .env
-include .env.local

.PHONY: tests

##@ Development commands

help: ## Show this help
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

install: ## Install dependencies in a virtualenv
	pipenv install --dev

freeze: ## Freeze requirements version for distribution
	pipenv lock -r > requirements

lint: ## Lint package using pylint
	# ~ lint style errors
	pipenv run flake8check
	# ~ lint missing documentation
	pipenv run pylintcheck

tests: ## Run tests sets
	pipenv run tests

twine: ## Manually build and distribute current version of package using twine
	pipenv run python setup.py sdist bdist_wheel
	pipenv run twine upload dist/*


##@ Deployment commands

stage: # Add commonly edited files to avoid manually commiting a minor change...
	git add .github/ README.md setup.cfg setup.py .gitignore Makefile Pipfile
	git commit -m "[DevOps] Prepare new version deployment" > /dev/null \
		|| echo "Nothing to commit, working tree clean"

patch: stage ## Deploy a new patch version of this package
	pipenv run bump2version patch
	git push && git push --tags

minor: stage ## Deploy a new minor version of this package
	pipenv run bump2version minor
	git push && git push --tags

major: stage ## Deploy a new patch version of this package
	pipenv run bump2version major
	git push && git push --tags
