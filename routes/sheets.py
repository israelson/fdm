from flask import Blueprint, render_template, request, redirect, url_for
from models.db_config import get_db_connection

sheets = Blueprint('sheets', __name__)

@sheets.route('/create_sheet', methods=['GET', 'POST'])
def create_sheet():
    if request.method == 'POST':
        character_name = request.form['character_name']
        manual = request.form['manual']
        attributes = request.form.getlist('attributes')
        movements = request.form.getlist('movements')
        story = request.form['story']
        inventory = request.form.getlist('inventory')
        relations = request.form.getlist('relations')

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO sheets (character_name, manual, attributes, movements, story, inventory, relations) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (character_name, manual, attributes, movements, story, inventory, relations)
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
    return render_template('sheet_list.html')
