from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

df = pd.DataFrame(
  [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
  ],
  columns=["a", "b", "c", "d"]
)

json_df = df.to_json(orient='values')

@app.route("/")
def index():
	df_values = df.values.tolist()   # 2次元配列（中身）
	df_columns = df.columns.tolist() # 1次元配列(ヘッダー)

	return render_template(
   'index.html',
		table=df.to_html(header='true')
  )

if __name__ == '__main__':
  app.run()