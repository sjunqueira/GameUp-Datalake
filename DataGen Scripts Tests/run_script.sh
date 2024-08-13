#!/bin/bash
# Ativar o ambiente virtual
source /home/sergio/dev/suslake/venv/bin/activate

# Verificar o Python usado
which python3 >> /home/sergio/dev/suslake/log.txt
python3 --version >> /home/sergio/dev/suslake/log.txt

# Executar o script Python
python3 /home/sergio/dev/suslake/tests.py >> /home/sergio/dev/suslake/log.txt 2>&1
