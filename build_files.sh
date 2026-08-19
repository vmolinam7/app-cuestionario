#!/bin/bash
echo "--- INICIANDO BUILD PARA VERCEL ---"
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
python3 manage.py migrate --noinput
python3 manage.py seed_preguntas
echo "--- BUILD COMPLETADO CON ÉXITO ---"
