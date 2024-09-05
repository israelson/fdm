from flask import Blueprint, render_template, request, redirect, url_for
from models.db_config import get_db_connection
import json

sheets = Blueprint('sheets', __name__)

@sheets.route('/create_sheet', methods=['GET', 'POST'])
def create_sheet():
    if request.method == 'POST':
        character_name = request.form.get('character_name', '')
        fighting_style = request.form.get('fighting_style', '')
        demeanor = request.form.get('demeanor', '')
        treinamento = request.form.get('treinamento', '')
        story = request.form.get('story', '')

        # Agrupar os atributos em um dicionário
        attributes = {
            "criatividade": request.form.get('creatividade', 0),
            "foco": request.form.get('foco', 0),
            "harmonia": request.form.get('harmonia', 0),
            "paixao": request.form.get('paixao', 0)
        }

        # Converter o dicionário para JSON
        attributes_json = json.dumps(attributes)

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO sheets (character_name, fighting_style, demeanor, story, attributes) "
            "VALUES (%s, %s, %s, %s, %s)",
            (character_name, fighting_style, demeanor, story, attributes_json)
        )
        sheet_id = cursor.lastrowid

        # Inserir movimentos selecionados
        movements = request.form.getlist('movements')
        movements_json = json.dumps(movements)  # Converter movimentos para JSON

        cursor.execute(
            "UPDATE sheets SET movements = %s WHERE id = %s",
            (movements_json, sheet_id)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('sheets.sheet_list'))

    return render_template('create_sheet.html')





@sheets.route('/sheets')
def sheet_list():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM sheets')
    sheets = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('sheet_list.html', sheets=sheets)

