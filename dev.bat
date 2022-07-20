@echo off

set opt=%1

if %opt%==backend (
	if not exist ".\tmp" md ".\tmp"
	if not exist ".\tmp\db" md ".\tmp\db"
	if not exist ".\tmp\db\backup" md ".\tmp\db\backup"
	if not exist ".\tmp\pyenv" md ".\tmp\pyenv"
	if not exist ".\tmp\data" md ".\tmp\data"
	if not exist ".\tmp\cache" md ".\tmp\cache"
	if not exist ".\tmp\cache\pypoetry" md ".\tmp\cache\pypoetry"
	docker-compose -f .\docker\docker-compose.dev.yml run -p 8000:8000 backend zsh
) else if %opt%==down (
	docker-compose -f docker/docker-compose.dev.yml down
) else (
	echo Usage: .\dev.bat backend|down
)

