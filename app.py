from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Initialize an empty list to store items
items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item_name = request.form['item_name']
    items.append(item_name)
    flash(f'Item "{item_name}" added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/edit/<int:item_index>', methods=['GET', 'POST'])
def edit_item(item_index):
    if request.method == 'POST':
        new_name = request.form['new_name']
        items[item_index] = new_name
        flash(f'Item updated to "{new_name}"!', 'success')
        return redirect(url_for('index'))
    item = items[item_index]
    return render_template('edit_item.html', item=item)

@app.route('/delete/<int:item_index>')
def delete_item(item_index):
    deleted_item = items.pop(item_index)
    flash(f'Item "{deleted_item}" deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
