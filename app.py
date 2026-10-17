from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Memuat model Random Forest cuaca yang sudah disimpan
model = joblib.load('weather_rf_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    # Ambil data fitur dari request JSON (23 kolom fitur)
    data = request.json['data']
    
    # Jalankan prediksi
    prediction = model.predict(data)
    
    # Kembalikan hasil (0: Tidak Hujan, 1: Hujan)
    return jsonify({
        'prediction': prediction.tolist()
    })

if __name__ == '__main__':
    app.run(debug=True)