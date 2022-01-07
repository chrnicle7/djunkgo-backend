"""
    Libraries
"""
from flask import request, Response, redirect, url_for
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from werkzeug.utils import secure_filename

from helper import GetCurrentUser
from models import UserToItem, Item

import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelBinarizer
import cv2
from tensorflow.keras.preprocessing.image import img_to_array

from main import db
import config as app_cfg
import os

"""
    Resource
"""

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])
  
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

class ScanImageResource(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        if "img" not in request.files :
            return {"message" : "Foto harus diupload"}, 400

        file = request.files["img"]
        if file.filename == "":
            return {"message" : "Nama file tidak boleh kosong"}, 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app_cfg.UPLOAD_FOLDER, filename)
            file.save(filepath)

            model_ml = PredictImage(filepath)
            model_ml.predict_image()

            item_found = Item.query.filter_by(nama=model_ml.result).first()

            new_pic = UserToItem(
                user_id = GetCurrentUser().get_current_user()["id"],
                item_id = item_found.id,
                percentage = round(model_ml.probabilty.item(), 2),
                path_foto=filepath,
                filename=filename,
                mimetype=file.mimetype,
            )
            db.session.add(new_pic)
            db.session.commit()

            return {
                "result": model_ml.result,
                "probability": str(round(model_ml.probabilty.item(), 2))
            }
        else:
            return {"message" : "Ekstensi foto yang diperbolehkan hanya png, jpg, jpeg, gif"}, 400



class PredictImage():
    
    def __init__(self, img_path):
        self.label_list=["Kaca piring","Botol plastik","Organik","Kertas","Plastik","Botol kaca","Metal","Kardus"]
        self.labels = np.array(self.label_list)
        self.lb = LabelBinarizer()
        self.labels = self.lb.fit_transform(self.labels)
        file_name = 'cv_model/junk91.h5'

        self.img_path = img_path
        self.result = ""
        self.probabilty = 0.0
        self.model = load_model(file_name)

    def predict_image(self):
        image = cv2.imread(self.img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        output = image.copy()
        image = cv2.resize(image, (224, 224))
        image = image.astype("float") / 255.0
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        proba = self.model.predict(image)[0]
        idx = np.argmax(proba)
        label = self.lb.classes_[idx]
        self.result = label
        self.probabilty = proba[idx]